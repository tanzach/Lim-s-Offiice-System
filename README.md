# ReadMe

### Create a virtual environment
- python -m venv (env name) 
  - ex. python -m venv msys42
 
### Activate virtual environment
- Windows: (env name)\Scripts\activate
- Mac: (env name)\bin\activate 

### Install Django and MySQL
- pip install django
- pip install mysqlclient

### Navigate to the directory with manage.py file 
- // cd (folder directory) 
- // cd .. to go back one directory
- // dir to show directories

### Make Migrations 
- python manage.py makemigrations 

### Migrate: 
- python manage.py migrate

### Runserver: 
- python manage.py runserver

### Make sure XAMPP is running the MYSQL server:
- database name: lims
- user: root 
- password: none 
