from rest_framework import serializers
from brand.models import BrandPlan, Promotion

from user.models import CustomerGoals

class UserPlanSubscribeSerializer(serializers.Serializer):
    plan_id = serializers.IntegerField()
    deposit_amount = serializers.IntegerField()
    user_id = serializers.IntegerField()


    def validate(self, attrs):
        print(attrs)
        if not BrandPlan.objects.filter(id = attrs['plan_id']):
            raise serializers.ValidationError("No such plan exists")
        if CustomerGoals.objects.filter(user_id_id = attrs['user_id'], plan_id = attrs['plan_id']):
            raise serializers.ValidationError("Already subscribed to this plan")
    
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

class SubscribeSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerGoals
        exclude = ['updated_at', 'start_date']
    
    def validate(self, attrs):
        return super().validate(attrs)