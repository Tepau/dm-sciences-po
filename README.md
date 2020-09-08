# Steps to follow to launch the project!

Project carried out for a job interview in **SciencesPo**

### Create a virtual environment and activate it

 - `python3 -m venv venv`
 - `source venv/bin/activate`

### Clone the repository

 - `git clone https://github.com/Tepau/dm-sciences-po.git`

### Install the project's dependencies

 - `cd dm-sciences-po`
 - `pip install -r requirements.txt`

### Create the migration file and launch migrations

 - `cd projet_dm`
 - `python manage.py makemigrations`
 - `python manage.py migrate`

### Upload data

 - `python manage.py loaddata tablets/dumps/tablets.json`

### Launch the server

 - `python manage.py runserver`

### Access to tablet lists

 - `/tablets/`
