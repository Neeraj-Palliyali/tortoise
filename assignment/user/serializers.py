from rest_framework import serializers
from brand.models import BrandPlan, Promotion

from user.models import CustomerGoals

class UserPlanSubscribeSerializer(serializers.ModelSerializer):
    plan_id = serializers.IntegerField()

    class Meta:
        model = CustomerGoals
        exclude = ['start_date', 'updated_at', 'plan_id']

    def validate(self, attrs):
        try:
            plan = BrandPlan.objects.get(id = attrs['plan_id'])
        except BrandPlan.DoesNotExist:
            raise serializers.ValidationError("No such plan exists")
        attrs['plan_id'] = plan
    
        return super().validate(attrs)

class UserPromotionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        exclude = ['created_at', 'updated_at']
    
    def to_representation(self, instance):
        return super().to_representation(instance)

class UserPlanListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BrandPlan
        exclude = ['created_at', 'updated_at']
    
    def to_representation(self, instance):
        
        return super(UserPlanListSerializer, self).to_representation(instance)
