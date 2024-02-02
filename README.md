# Django Mailer 'ТИЧЕР'
Этот репозиторий содержит конфигурацию Docker Compose для запуска Django-приложения с Celery и Redis. В настройках также предусмотрена база данных PostgreSQL для хранения данных.

## Установка Docker

1) Убедитесь, что у вас установлены Docker и Docker Compose на вашем компьютере.
- [Руководство по установке Docker](https://docs.docker.com/engine/install/ubuntu/)

2) Использование
Клонируйте репозиторий на ваш компьютер.

```bash
git clone <repository-url>
cd <repository-directory>
```

3) Создайте файл `.env` на основе `.env.sample` и заполните его:
```bash
touch django_drf_hw/.env
echo django_drf_hw/.env.sample > django_drf_hw/.env
vim django_drf_hw/.env
```

4) Запустите приложение с помощью Docker Compose.

```bash
docker-compose up --build
```

Доступ к Django-приложению по адресу http://localhost:8001.

Замечания
- Django-приложение настроено на работу на порту 8001, чтобы избежать конфликтов с локальным сервером разработки.
- Сервисы Celery Worker и Beat настроены на запуск с Django-приложением и зависят от сервисов web и redis.



## Установка вручную

1) Убедитесь, что у вас установлен Python3 и Django.

2) Склонируйте репозиторий:
```bash
git clone https://github.com/Dadoxr/django_drf_hw.git
cd django_drf_hw
```

3) Активируйте виртуальное окружение:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

4) Создайте файл `.env` на основе `.env.sample` и заполните его:
```bash
touch django_drf_hw/.env
echo django_drf_hw/.env.sample > django_drf_hw/.env
vim django_drf_hw/.env
```


5) Создайте базу данных, если ее нет:
```bash
psql -U postgres
CREATE DATABASE DB_NAME;
\q
```

7) Примените миграции:
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

8) Создайте все типы юзеров и наполните модел приложения `edu`:
```bash
python3 manage.py csu
python3 manage.py loaddata edu.json
```

8) Запустите сервис:
```bash
python3 manage.py runserver
```


## эндпоинты
- **ViewSet**: http://127.0.0.1:8000/edu/course/ 
- **Ограниченный ViewSet (только PUT, PATCH)**: http://127.0.0.1:8000/edu/users/1 

- **Generics**: 
    - http://127.0.0.1:8000/edu/lesson/create/
    - http://127.0.0.1:8000/edu/lesson/list/
    - http://127.0.0.1:8000/edu/lesson/get/1
    - http://127.0.0.1:8000/edu/lesson/update/
    - http://127.0.0.1:8000/edu/lesson/delete/
    