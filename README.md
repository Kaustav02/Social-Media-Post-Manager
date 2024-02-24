# Social-Media-Post-Manager

This is a Django web application for managing posts and user activity.

## Technologies Used

- **Django**: Python web framework for backend development.
- **Flexmonster Pivot Table & Charts**: JavaScript library for creating charts.
- **HTML/CSS**: Frontend markup and styling.
- **SQLite**: Database for storing user and post data.
- **Bootstrap**: Frontend framework for responsive design.

## Features

- User authentication and authorization.
- CRUD operations for posts.
- Dashboard with user activity chart.

## Installation

1. Clone the repository
2. Navigate to the project directory
3. Create a virtual environment : `python -m venv env`
4. Activate the virtual environment: On Windows
`env\Scripts\activate`
On macOS/Linux
`source env/bin/activate`
5. Apply migrations : `python manage.py migrate`
6. Create a superuser (for accessing admin panel) : `python manage.py createsuperuser`
7. Run the development server : `python manage.py runserver`


The project will be available at http://127.0.0.1:8000/.

## Usage

1. Visit the website and sign up for an account.
2. Log in with your credentials.
3. Create, view, update, or delete posts.
4. Navigate to the dashboard to view your activity chart.


