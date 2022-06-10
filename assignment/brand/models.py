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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.plan_name
    
class Promotion(models.Model):
    plan = models.ForeignKey(BrandPlan, on_delete= models.CASCADE)
    name = models.CharField(max_length=50)
    user_limit = models.IntegerField(blank= True, null= True)
    expiry_date = models.DateField(blank= True, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name