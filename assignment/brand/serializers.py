from pyexpat import model
from rest_framework import serializers

from .models import BrandPlan, Promotion


class PlanSerialiezer(serializers.ModelSerializer):
    
    class Meta:
        model = BrandPlan
        exclude = ['created_at', 'updated_at', 'is_user_limited', 'is_date_limited']

    def validate(self, attrs):
        return super().validate(attrs)

class PlanListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BrandPlan
        exclude = ['created_at', 'updated_at']
    
    def to_representation(self, instance):
        return super(PlanListSerializer, self).to_representation(instance)


class PlanIdSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Promotion
        exclude = ['created_at','updated_at']

    def validate(self, attrs):
        if 'id' in attrs:
            try:
                BrandPlan.objects.get(attrs['id'])
            except BrandPlan.DoesNotExist:
                raise serializers.ValidationError("No such plan exists")
        if not ('expiry_date' in attrs or 'user_limit' in attrs):
            raise serializers.ValidationError("Either expiry_date or user_limit is required")

        return super().validate(attrs)
