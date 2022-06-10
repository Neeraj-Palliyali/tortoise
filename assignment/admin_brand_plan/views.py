from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated

from .serializers import PlanSerialiezer
# Create your views here.

class AdminPlanViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlanSerialiezer
    def create(self, request, *args, **kwargs):
        print(request.data)
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