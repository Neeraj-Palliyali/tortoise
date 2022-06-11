from rest_framework import serializers
from brand.models import BrandPlan, Promotion

from user.models import CustomerGoals

class UserPlanSubscribeSerializer(serializers.Serializer):
    plan_id = serializers.IntegerField()
    deposit_amount = serializers.IntegerField()
    user_id = serializers.IntegerField()


    def validate(self, attrs):
        # Check if a plan exits
        if not BrandPlan.objects.filter(id = attrs['plan_id']):
            raise serializers.ValidationError("No such plan exists")
        # cannot Subscribe to a plan more than once
        if CustomerGoals.objects.filter(user_id_id = attrs['user_id'], plan_id = attrs['plan_id']):
            raise serializers.ValidationError("Already subscribed to this plan")
    
        return super().validate(attrs)

class UserPlanListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BrandPlan
        exclude = ['created_at', 'updated_at', 'benefit_percent']
    
    def to_representation(self, instance):
        representation = super(UserPlanListSerializer, self).to_representation(instance)
        promos = Promotion.objects.filter(plan_id = instance.id, is_active =  True)
        # Promotional benefit percentage
        if promos:
            representation['benefit_percent'] =  promos[0].benefit_percent 
        else:
            representation['benefit_percent'] = instance.benefit_percent
        return representation

class SubscribeSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerGoals
        exclude = ['updated_at', 'start_date']
    
    def validate(self, attrs):
        return super().validate(attrs)