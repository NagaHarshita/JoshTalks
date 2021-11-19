## Youtube Videos - Backend Task 


### Installing necessary libraries and running the server

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
```
redis-cli ping
-> PONG
```

- Start celery and celery-beats in different terminals for running periodic tasks in the background
```
celery -A JoshTalks.celery worker --pool=solo -l info 
```
```
celery -A JoshTalks beat -l INFO
```

### API testing

- Navigate to 'http://127.0.0.1:8000/videos/' to view the user interface with fetched videos in a paginated manner 
- Perform a get request to "http://127.0.0.1:8000/youtube/api/videos/" url then you can get the list of all the videos
- Perform a get request to 'http://127.0.0.1:8000/youtube/api/search/?title=Autumn%20Friday' to enter your query and get the results

Please check the django admin to view the changing objects inside Videos for every 300sec. 

Make sure to terminate the celery-beats command as the quota for youtube may exceed.