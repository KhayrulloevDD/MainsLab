from django.urls import path
from file_uploader.apis import upload_excel_files, get_clients, filter_bills

urlpatterns = [
    path('upload_excel_files', upload_excel_files, name='upload_excel_files'),
    path('get_clients', get_clients, name='get_clients'),
    path('filter_bills', filter_bills, name='filter_bills'),
]
