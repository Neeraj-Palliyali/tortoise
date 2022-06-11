from celery import shared_task
from datetime import datetime
from .models import Promotion

# To set all expired promotions to inactive
@shared_task(bind = True)
def expiry_promotion_daily(self):
    promos = Promotion.objects.filter(expiry_date = datetime.now().date() )
    for promo in promos:
        promo.is_active = False
        promo.save()
    return {"sucess":"True", "message":"Promotions with expiry is set to inactive"}