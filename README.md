Инструкции по разворачиванию:

- Клонируйте репозиторию https://github.com/KhayrulloevDD/MainsLab.git;
- Создайте виртуальное окружение и активируйте его (необъязательно);
- Установить зависимости из файла requirements.txt (pip install -r requirements.txt);
- Мигрируйте миграции (python manage.py migrate);
- Создайте администратора (python manage.py createsuperuser)(необъязательно);
- Запустите локальный сервер (python manage.py runserver).

Инструкции по использованию:
 - POST: http://127.0.0.1:8000/api/file_uploader/upload_excel_files
   
       body:
       {
            "client_org": файл client_org.xlsx,
            "bills": файл bills.xlsx
       }
   
       Ответ:
       {
          "status": "Success",
          "data": [
              {
                  "client_name": 1,
                  "client_org": 1,
                  "number": 1.0,
                  "summary": 10000.0,
                  "date": "2021-04-01",
                  "service": "вызов врача на дом",
                  "fraud_score": 0.16,
                  "service_class": 2,
                  "service_name": "лечение"
              }
               ...
         ]
       }
   
- GET: http://127.0.0.1:8000/api/file_uploader/get_clients
       
      Ответ:
       [
          {
              "id": 1,
              "name": "client1",
              "organization_number": 2,
              "debit": 191906.55000000002
          },
          {
              "id": 2,
              "name": "client2",
              "organization_number": 1,
              "debit": 14777.0
          },
          {
              "id": 3,
              "name": "client3",
              "organization_number": 0,
              "debit": null
          }
      ]
- POST: http://127.0.0.1:8000/api/file_uploader/filter_bills
      body:
       {
            "client_name": "client1",
            "client_org": "OOO Client1Org1"
       }
   
       Ответ:
       [
          {
              "id": 1,
              "client_name": 1,
              "client_org": 1,
              "number": 1,
              "summary": 10000.0,
              "date": "2021-04-01",
              "service": "вызов врача на дом",
              "fraud_score": 0.16,
              "service_class": 2,
              "service_name": "лечение"
          },
               ...
       ]
