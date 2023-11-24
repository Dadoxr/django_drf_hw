# Django Mailer 'ТИЧЕР'

Думаю что написать

## Установка

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
    