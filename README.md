<h3><b>Что это:</b></h2>

В 2018 году Джеймс Клир написал книгу «Атомные привычки», которая посвящена приобретению новых полезных привычек и 
искоренению старых плохих привычек. Данное приложение рассылает напоминания в телеграм бот о необходимости выполнить 
привычку в указанное время в указанном месте, является API сервером. 

<h3><b>Как установить:</b></h2>
Склонируйте/скачайте проект, активируйте виртуальное окружение проекта (python -m venv venv), установите необходимые библиотеки - pip install -r requirements.txt 
Установите на свою ОС WSL и запустите redis - https://redis.io/docs/getting-started/installation/install-redis-on-windows/ 

<h3><b>Перед началом:</b></h2>

Необходимо создать и внести свои данные в файл .env (необходимые данные в .env_sample)

Создание базы данных:
- psql -U postgres

- CREATE DATABASE <database_name>;

- python manage.py migrate

Для создания суперпользователя:
- python manage.py csu

- Данные суперпользователя можно изменить в - <b>user/management/commands/csu.py</b>

<h3><b>Как оно работает:</b></h2>

Для запуска приложения > <b>python manage.py runserver</b>

Запуск рассылки - celery -A config beat -l INFO 

Убедись, что у тебя установлен Docker - <b>docker --version</b>
Для сборки образов используй команду - <b>docker-compose build</b>
Для запуска контейнеров - <b>docker-compose up</b>

