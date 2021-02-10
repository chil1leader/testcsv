Инструкция по запуску:

1)Загрузить проект в виде zip-файла. Распаковать папку "testcsv-main" и открыть ее с помощью bash или либо другой вариации из командных оболочек.


3)Выполнить команду запуска проекта: 
                      
                      docker-compose up -d

4)Выполнить миграции: 

                      docker-compose exec web python manage.py makemigrations deals
                      
                      docker-compose exec web python manage.py migrate

Маршрутизация:

1)http://localhost:8000/api/upload/ - Загрузка файла формата .csv для обработки. Выбрать файл 'deals.csv' для POST-запроса.

2)http://localhost:8000/api/list/ - Выдача обработанных данных
