from rest_framework import serializers
from file_uploader.models import Client, Organization, Bill


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'name', ]


class OrganizationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organization
        fields = ['id', 'client_name', 'name', 'address', ]


class BillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bill
        fields = ['id', 'client_name', 'client_org', 'number', 'summary', 'date', 'service',
                  'fraud_score', 'service_class', 'service_name', ]
