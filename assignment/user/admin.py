from django.contrib import admin

from user.models import CustomerGoals

# Register your models here.
class SubscriptionAdmin(admin.ModelAdmin):
    list_display=('user_id','benefit_percentage')

admin.site.register(CustomerGoals, SubscriptionAdmin)