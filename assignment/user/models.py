from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from brand.models import BrandPlan
from utils.constants import AMOUNT_CHOICES, BENEFIT_CHOICES

# Create your models here.

class CustomerGoals(models.Model):
    plan_id  = models.ForeignKey(BrandPlan, on_delete= models.DO_NOTHING)
    user_id  = models.ForeignKey(User, on_delete= models.DO_NOTHING)
    selected_amount = models.IntegerField(choices= AMOUNT_CHOICES)
    selected_tenure = models.IntegerField(default=1, validators=[
        MaxValueValidator(60),
        MinValueValidator(1)
        ])
    deposit_amount = models.BigIntegerField()
    benefit_percentage = models.FloatField()
    benefit_type = models.CharField(choices=BENEFIT_CHOICES, max_length=1)
    start_date = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)