from pyexpat import model
from statistics import mode
from rest_framework import serializers

from .models import BrandPlan, Promotion


class PlanSerialiezer(serializers.ModelSerializer):
    
    class Meta:
        model = BrandPlan
        exclude = ['created_at', 'updated_at',]

    def validate(self, attrs):
        return super().validate(attrs)

class PlanListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BrandPlan
        exclude = ['created_at', 'updated_at']
    
    def to_representation(self, instance):
        return super(PlanListSerializer, self).to_representation(instance)


class PlanIdSerializer(serializers.ModelSerializer):
    plan_id = serializers.IntegerField()

    class Meta:
        model = Promotion
        exclude = ['created_at','updated_at','is_active', 'plan']

    def validate(self, attrs):
        
        if not BrandPlan.objects.filter(id = attrs['plan_id']):
            raise serializers.ValidationError("No such plan exists")
        promos = Promotion.objects.filter(plan_id = attrs['plan_id'])
        for promo in promos:
            if promo.is_active:
                raise serializers.ValidationError("A brand cannot have more than one active promotions")
        if not ('expiry_date' in attrs or 'user_limit' in attrs):
            raise serializers.ValidationError("Either expiry_date or user_limit is required")
        return super().validate(attrs)

class PromotionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        exclude = ['created_at', 'updated_at','is_active']

    def validate(self, attrs):
        return super().validate(attrs)

class PromotionListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Promotion
        exclude = ['created_at', 'updated_at']
    
    def to_representation(self, instance):
        return super(PromotionListSerializer, self).to_representation(instance)

