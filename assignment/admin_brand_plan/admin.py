from django.contrib import admin

from .models import BrandPlan

# Register your models here.

class PlanAdmin(admin.ModelAdmin):
    list_display= ('id','plan_name',)

admin.site.register(BrandPlan, PlanAdmin)