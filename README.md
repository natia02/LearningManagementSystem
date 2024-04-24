# Learning management system

This is a Django project for learning management system

## Prerequisites

- Python (version 3.12.2)
- Django (version 5.0.3)

1. Clone the repository: 
    ```bash
    git clone https://github.com/natia02/LearningManagementSystem.git
    ```
2. Navigate to the project directory: 
    ```bash
    cd LearningManagementSystem
    ```

3. Create and activate a virtual environment: 
    ```bash
    python -m venv env
    env\Scripts\activate
    ```

4. Install the required dependencies: 
    ```bash
    pip install -r requirements.txt
    ```

5. Create a superuser: 
    ```bash
    python manage.py createsuperuser
    ```
   and follow instructions

6. Start the development server: 
    ```bash
    python manage.py runserver
    ``` 
The application should now be accessible at `http://127.0.0.1:8000/` this is the main page 

From the page `http://127.0.0.1.8000/admin` you can log in as a superuser.

username and passwords of registered students are email and "name123/name/" like for me, 
it would be name123Natia
