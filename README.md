Инструкция по запуску:

1)Распаковать папку "testcsv-main" и открыть ее с помощью bash или либо другой вариации из командных оболочек.


2)Выполнить команду запуска проекта: 
                      
                      docker-compose up -d

3)Выполнить миграции: 

                      docker-compose exec web python manage.py makemigrations deals
                      
                      docker-compose exec web python manage.py migrate

Маршрутизация:

1)http://localhost:8000/api/upload/ - Загрузка файла для обработки

2)http://localhost:8000/api/list/ - Выдача обработанных данных
