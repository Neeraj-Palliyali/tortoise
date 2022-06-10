from django.contrib import admin

from .models import BrandPlan, Promotion

# Register your models here.

class PlanAdmin(admin.ModelAdmin):
    list_display= ('id','plan_name',)

class PromotionAdmin(admin.ModelAdmin):
    list_display= ('id','name','plan', )

admin.site.register(BrandPlan, PlanAdmin)
admin.site.register(Promotion, PromotionAdmin)