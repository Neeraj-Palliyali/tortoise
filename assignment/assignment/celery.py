from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assignment.settings')
app = Celery('assignment')


app.config_from_object(settings, namespace= 'CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'every-day':{
        'task':'brand.tasks.expiry_promotion_daily',
        'schedule':crontab(minute = 45, hour = 9,)
    }
}


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))