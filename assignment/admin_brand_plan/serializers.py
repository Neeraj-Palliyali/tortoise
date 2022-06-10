from rest_framework import serializers

from .models import BrandPlan


class  PlanSerialiezer(serializers.ModelSerializer):
    
    class Meta:
        model = BrandPlan
        exclude = ['created_at', 'updated_at', 'is_user_limited', 'is_date_limited']

    def validate(self, attrs):
        if 'user_limit' in attrs:
            attrs.update({'is_user_limited':True})
        elif 'expiry_data' in attrs:
            attrs.update({'is_date_limited':True})
        else:
            raise serializers.ValidationError("No limits (user limit or expiry date specified)")
        return super().validate(attrs)