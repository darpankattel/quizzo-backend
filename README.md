
![Quizzo](https://cdn.discordapp.com/attachments/1068705541058199606/1206289261670834206/logo-full.png?ex=65db776b&is=65c9026b&hm=3443a05cf71f31ff59edbbbbd62b7b85e2a14192d56e6b9e43b6084cba461b2b&)
# Quizzo - Showcase your knowledge

## Introduction

Welcome to Quizzo, a web application designed to bring the thrill of quizzes to your fingertips. With a diverse range of quiz categories and levels, Quizzo offers an engaging experience for users to test their knowledge, earn experience points (XP), and compete with others.

## Tech Stack
**1. Python Django**: Quizzo is powered by Django, a high-level Python web framework that facilitates rapid development and clean, pragmatic design.

**2. SQLite**: The backend database management system used for storing quiz data and user information.

**3. Django REST Framework**: Leveraging the capabilities of Django REST Framework to build robust APIs, enabling seamless communication between the frontend and backend components.

Get ready to embark on a journey of learning and fun with Quizzo!

## Running the Django App
This guide will walk you through the steps to run the Quizzo Django project locally on your machine.

### 1. Installing Django
Ensure you have Python installed on your system. If not, you can download and install it from the [official Python website](https://www.python.org/).

Once Python is installed, you can install Django using pip, Python's package installer. Open your terminal or command prompt and run the following command:

```python
pip install django
```

### 2. Setting up the project
Clone the Quizzo project repository from GitHub:
```
git clone https://github.com/darpankattel/quizzo-frontend.git
```
Navigate to the projects directory
```
cd quizzo
```
You will find there a `requirements.txt` file and `manage.py` file.

**Create a virtual environment and then activate it.** *You may install venv from pip, then use it to create a virtual environment*

Then, install the dependencies:
```python
pip install -r requirements.txt
```
Once dependencies are installed, you can start the Django development server by running the following command:
```python
python manage.py runserver
```
By default, the server will run on [http://127.0.0.1:8000/](http://127.0.0.1:8000). You can access the Quizzo application by visiting this URL in your web browser.

*You may need to make or migrate the migrations as required.*

### 3. Accessing the Admin Panel

To access the Django admin panel, create a superuser account by running:

```python
python manage.py createsuperuser

```
Follow the prompts to create a username, email, and password for the superuser account.

Once the superuser account is created, you can access the admin panel by visiting [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) in your web browser and logging in with the superuser credentials.