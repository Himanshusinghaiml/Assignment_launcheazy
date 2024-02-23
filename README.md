## Assignment User management System
```
Problem Statement :- 
Develop a user management system for a platform that supports multiple organizations. Each
organization can have multiple users with different roles. The system should handle user sign-up, role
management, and organization membership requests.
```
1. for Run the Assignment follow commands :-
# Navigate to Your Project Directory:

Open a terminal or command prompt.
Navigate to the directory where your Assignment-launcheasy file is located.
2. Make a virtualenv for dependencies
`python -m venv assignenv`
then type :-
   `assignenv\scripts\activate.bat`
3. then run the commands 
  ` pip install -r requirements.txt`
4. run two commands for make a model 
 ` python manage.py makemigrations`
 ` python manage.py migrate`
5. run the server
` python manage.py runserver `