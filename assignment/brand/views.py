from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated

from utils.pagination import PlanListPagination

from .serializers import PlanIdSerializer, PlanListSerializer, PlanSerialiezer
from .models import BrandPlan, Promotion
# Create your views here.

class BrandPlanViewset(viewsets.ModelViewSet):
    
    permission_classes = (IsAuthenticated,)
    serializer_class = PlanSerialiezer
    pagination_class = PlanListPagination

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data =  request.data)
        if (serializer.is_valid(raise_exception=True)):
            serializer.save()
        return Response(
            {
                "success":True,
                "message":f"Created Plan with name: {request.data.get('plan_name')}"
            },
            status= status.HTTP_201_CREATED
        )
    
    def list(self, request, *args, **kwargs):
        print(request.user.username)
        plans = BrandPlan.objects.all()
        if plans:
            page = self.paginate_queryset(plans)
            if page is not None:
                serializer = PlanListSerializer(plans, many = True)
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
                }, status= status.HTTP_200_OK
            )


class PromotionViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = PlanIdSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        plan = BrandPlan.objects.get(id = request.data.get('id'))
        
        return super().create(request, *args, **kwargs)