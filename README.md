# Tortoise

I have used postgres for db.
<br />
Celery and Celery beat is also running as workers for auto expiry
<br />
Creating a db in postgres with 'tortoise' name is required and changing the broker url based on you choices
<br />
# Steps for installation

Step1:get into assignment directory
Step2:django runserver
```
python manage.py runserver
```
Step3: start celery worker
```
celery -A assignment.celery worker --pool=solo -l info
```
Step4: start celery beat
```
celery -A assignment beat
```
Step5: Setup complete now use login api to login and get the bearer token
  ps: All the api calls are added as a postman collection 
Step6: Use the token to call all other required api calls from the collection

