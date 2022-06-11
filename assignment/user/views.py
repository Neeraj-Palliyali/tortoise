from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from brand.models import BrandPlan, Promotion

from utils.pagination import PlanListPagination
from .serializers import SubscribeSaveSerializer, UserPlanListSerializer, UserPlanSubscribeSerializer
# Create your views here. 

class BrandPlanViewset(viewsets.ModelViewSet):
    
    permission_classes = (IsAuthenticated,)
    serializer_class = UserPlanListSerializer
    pagination_class = PlanListPagination

    def create(self, request, *args, **kwargs):
        # Creating subscriptions to brand plans
        # Assuming user can subscribe to more than one plan  
        # but can only subscribe to one brand plan once
        data = request.data
        data.update({"user_id":request.user.id})
        serialzer = UserPlanSubscribeSerializer(data = request.data)
        serialzer.is_valid(raise_exception= True)
        data = serialzer.data
        plan = BrandPlan.objects.get(id = data['plan_id'])
        # one promotion can only be active for one pan
        promotion = Promotion.objects.filter(id = plan.id, is_active = True)
        # Getting the promotion benefit percentage
        if promotion:
            benefit = promotion[0].benefit_percent
        else:
            benefit = plan.benefit_percent
        data.update(
            {
                "plan_id" : plan.id,   
                "selected_amount": plan.amount_options,
                "selected_tenure":plan.tenure_options,
                "benefit_percentage":benefit,
                "benefit_type":plan.benefit_type

            }
        )
        save_serializer = SubscribeSaveSerializer(data = data)
        save_serializer.is_valid(raise_exception=True)
        save_serializer.save()

        # If this user is the last user that can subscribe to a promotion
        if promotion:
            if promotion[0].user_limit:
                promotion[0].user_limit -=1
                promotion[0].is_active = False if promotion[0].user_limit == 0 else True 
                promotion[0].save()

        return Response( 
            { "success" : True,
            "message":"User Subscribed" 
            },status= status.HTTP_201_CREATED
        )


    def list(self, request, *args, **kwargs):
        # listing all plans paginated with promotion benefit percentage
        plans = BrandPlan.objects.all()
        if plans:
            page = self.paginate_queryset(plans)
            if page is not None:
                # Pagnation for user plans
                serializer = UserPlanListSerializer(plans, many = True)
                page_data = self.get_paginated_response(serializer.data).data
            
            return Response(
                {
                "success":True,
                "messages":"The plans are",
                "data":page_data
                }, status= status.HTTP_200_OK
            ) 
        else:
            return Response(
                {
                    "success":False,
                    "message":"No plans"
                }, status= status.HTTP_400_BAD_REQUEST
            )
