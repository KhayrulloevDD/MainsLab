from django.contrib import admin
from file_uploader.models import Client, Organization, Bill


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    ordering = ['id']


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['id', 'client_name', 'name', 'address', 'fraud_weight', ]
    ordering = ['id']


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ['id', 'client_name', 'client_org', 'number', 'summary', 'date', 'service',
                    'fraud_score', 'service_class', 'service_name', ]
    ordering = ['id']
    list_filter = ['client_name', 'client_org', ]
