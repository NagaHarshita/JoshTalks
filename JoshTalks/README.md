## Youtube Videos - Backend Task 


### Installing necessary libraies and running the server

- Create the virtual environment 
```
cd JoshTalks
python3 -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

- Start the django-server
```
python3 manage.py migrate 
python3 manage.py makemigrations
python3 manage.py createsuperuser 
python3 manage.py runserver 
```

- Start redis 
redis-cli ping should respond PONG in the terminal

- Start celery and celery-beats in different terminals for periodic tasks
```
celery -A JoshTalks.celery worker --pool=solo -l info 
```
```
celery -A JoshTalks beat -l INFO
```

### API testing 

- Navigate to 'videos/' to view the fetched videos in a paginated manner 
- Navigate to 'search/' to enter your query and get the answer

