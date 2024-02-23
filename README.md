# User Management System

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies](#technologies)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction
The User Management System is a platform designed to manage users, roles, and organizations. It allows organizations to register and manage their members, assign roles to users, and handle membership requests. This README provides information on how to set up and use the system.

## Features
- User Sign-up: Users can sign up with their organizations and request membership.
- Role Management: Admins can create roles and assign them to users within their organization.
- Organization Management: Organizations can manage their members and membership requests.
- Billing Group: Organizations are associated with billing groups that determine the maximum number of users allowed.

## Technologies
- Python
- Django
- Django REST Framework
- PostgreSQL/MySQL (RDBMS)

## Setup
1. Clone the repository to your local machine.

2. **Navigate to Your Project Directory**:
   - Open a terminal or command prompt.
   - Navigate to the directory where your `Assignment-launcheasy` file is located.

3. **Create a Virtual Environment for Dependencies**:
   - Use the following command to create a virtual environment:
     ```
     python -m venv assignenv
     ```
   - Activate the virtual environment:
     - For Windows:
       ```
       assignenv\Scripts\activate.bat
       ```
 
5. Install dependencies:
   ``` pip install -r requirements.txt```

6. Apply database migrations:
- ``` python manage.py makemigrations```

7. ``` python manage.py migrate```

## Usage
1. Start the development server:
2. Access the application in your web browser at `http://127.0.0.1:8000/`.
3. Sign up, manage roles, and handle organization memberships through the provided interfaces.


