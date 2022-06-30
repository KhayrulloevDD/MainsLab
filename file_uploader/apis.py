from django.db.models import Sum
from django.utils.datastructures import MultiValueDictKeyError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from file_uploader.services import parse_client_org_xlsx_file, parse_bills_xlsx_file, replace_client_name_to_client_id, \
    replace_client_name_and_client_org_to_ids, count_fraud_weight
from file_uploader.models import Client, Organization, Bill
from file_uploader.serializers import ClientSerializer, OrganizationSerializer, BillSerializer


@api_view(['POST'])
def upload_excel_files(request):
    try:
        client_org_file = request.FILES['client_org']
        client_org_response_data = parse_client_org_xlsx_file(client_org_file)

        client_serializer = ClientSerializer(data=client_org_response_data['clients'], many=True)
        if client_serializer.is_valid(raise_exception=True):
            client_serializer.save()

        # get clean data of organizations
        organizations = replace_client_name_to_client_id(client_org_response_data['organizations'],
                                                         client_serializer.data)

        organization_serializer = OrganizationSerializer(data=organizations, many=True)
        if organization_serializer.is_valid(raise_exception=True):
            organization_serializer.save()

        bills_file = request.FILES['bills']
        bills_response_data = parse_bills_xlsx_file(bills_file)

        # get clean data of bills
        bills = replace_client_name_and_client_org_to_ids(bills_response_data['bills'],
                                                          client_serializer.data,
                                                          organization_serializer.data)

        bill_serializer = BillSerializer(data=bills, many=True)
        if bill_serializer.is_valid(raise_exception=True):
            bill_serializer.save()

        count_fraud_weight()

        return Response({"status": "Success", "data": bills}, status=status.HTTP_201_CREATED)

    except MultiValueDictKeyError:
        return Response({"file": "Файл не был загружен"}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"status": "Error", "message": f"в процессе обработки файла произошла ошибка: {e}"},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_clients(request):
    clients = Client.objects.all()
    serializer = ClientSerializer(clients, many=True)
    for client in serializer.data:
        client['organization_number'] = Organization.objects.filter(client_name=client['id']).count()
        client['debit'] = Bill.objects.filter(client_name=client['id']).aggregate(Sum('summary'))['summary__sum']
    return Response(serializer.data)


@api_view(['POST'])
def filter_bills(request):
    filters = dict()
    if request.data['client_name']:
        filters['client_name__name'] = request.data['client_name']
    if request.data['client_org']:
        filters['client_org__name'] = request.data['client_org']

    bills = Bill.objects.filter(**filters)
    serializer = BillSerializer(bills, many=True)
    return Response(serializer.data)
