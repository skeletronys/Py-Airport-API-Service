# Py-Airport-API-Service

## Project Overview

Py-Airport-API-Service is a RESTful web service designed to manage airports, flights, tickets, and orders. It provides a robust backend infrastructure using Django and Django REST framework.

### Technology Stack

- **Python**: Programming language used for backend development.
- **Django**: Web framework for building web applications in Python.
- **Django REST framework**: Toolkit for building Web APIs in Django.
- **SQLite**: Relational database management system used by default with Django.

### Installation

1. **Clone the repository:**

    ```sh
    git clone <repository_url>
    cd Py-Airport-API-Service
    ```

2. **Setup Virtual Environment:**

    ```sh
    python -m venv .venv
    .venv\Scripts\activate  # For Windows
    source .venv/bin/activate  # For Linux/MacOS
    ```

3. **Install Dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set Environment Variables:**

    Create a `.env` file in the root directory with the following content:

    ```env
    SECRET_KEY=your_secret_key_here
    ```

    Replace `your_secret_key_here` with a secure random string. You can generate one at [djecrety.ir](https://djecrety.ir).

5. **Apply Migrations:**

    ```sh
    python manage.py migrate
    ```

6. **Run the Development Server:**

    ```sh
    python manage.py runserver
    ```

    The API will be accessible at `http://localhost:8000`.

### Testing

To run tests, execute the following command:

    ```sh
    python manage.py test
    ```
