# Py-Airport-API-Service

## Опис проекту

Py-Airport-API-Service – це RESTful веб-сервіс для управління аеропортами, рейсами, квитками та замовленнями.

### Технологічний стек

- Python
- Django
- Django REST framework
- SQLite

### Встановлення

1. Клонуйте репозиторій:
    ```sh
    git clone <repository_url>
    ```

2. Перейдіть в каталог проекту:
    ```sh
    cd Py-Airport-API-Service
    ```

3. Створіть та активуйте віртуальне оточення:
    ```sh
    python -m venv .venv
    .venv\Scripts\activate  # Windows
    source .venv/bin/activate  # Linux/MacOS
    ```

4. Встановіть залежності:
    ```sh
    pip install -r requirements.txt
    ```

5. Створіть файл `.env` в кореневому каталозі та додайте змінну `SECRET_KEY`:
    ```env
    SECRET_KEY=your_dummy_secret_key
    ```

6. Застосуйте міграції:
    ```sh
    python manage.py migrate
    ```

7. Запустіть сервер:
    ```sh
    python manage.py runserver
    ```

### Інструкції з тестування

1. Створіть тестову базу даних та запустіть тести:
    ```sh
    python manage.py test
    ```
