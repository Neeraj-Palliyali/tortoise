from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from brand.models import BrandPlan

from utils.pagination import PlanListPagination
from .serializers import UserPlanListSerializer, UserPlanSubscribeSerializer
# Create your views here. 

class BrandPlanViewset(viewsets.ModelViewSet):
    
    permission_classes = (IsAuthenticated,)
    serializer_class = UserPlanListSerializer
    pagination_class = PlanListPagination

    def create(self, request, *args, **kwargs):
        serialzer = UserPlanSubscribeSerializer(data = request.data)
        serialzer.is_valid(raise_exception= True)
        serialzer.save()
        return Response( { "success" : "HEHE" })


    def list(self, request, *args, **kwargs):
        print(request.user.username)
        plans = BrandPlan.objects.all()
        if plans:
            page = self.paginate_queryset(plans)
            if page is not None:
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
