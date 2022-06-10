from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class BrandPlan(models.Model):
    BENEFIT_CHOICES = (
        ("C", "Cash Back"),
        ("V", "Extra Voucher"),
    )
    plan_name = models.CharField(max_length=50)
    amount_options = models.FloatField()
    tenure_options = models.IntegerField(default=1, validators=[
        MaxValueValidator(60),
        MinValueValidator(1)
        ])
    benefit_options = models.IntegerField(verbose_name="percentage",
        default=0, validators=[
        MaxValueValidator(100),
        MinValueValidator(1)
        ]
    )
    benefit_type = models.CharField(max_length=1 , choices=BENEFIT_CHOICES)
    is_user_limited = models.BooleanField(default=False)
    is_date_limited = models.BooleanField(default=False)
    user_limit = models.IntegerField(blank= True, null= True)
    expiry_data = models.DateField(blank= True, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)