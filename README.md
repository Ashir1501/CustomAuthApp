## Custom User model for Authentication using Django Framework and Blog App
* I use python's virtualenv library to isolate the dependencies
### Virtual Environment Setup
* using pip install virtualenv
* create virtual environment using -> python3 -m venv venv-name
* Now to activate it -> . venv-name/bin/activate
* Install libraries/dependencies after activating virtual env
* To deactivate -> deactivate

### Steps to run the project
* Since this projct uses mysql database makesure to install mysqlclient using pip and configure database settings in settings.py
* using pip install django==4.2.0, pillow
* run -> python manage.py makemigrations
* run -> python manage.py migrate
* run -> python manage.py runserver
  
