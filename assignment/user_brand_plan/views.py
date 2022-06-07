from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class brand_plan(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    # def create(self, request, *args, **kwargs):
    #     return super().create(request, *args, **kwargs)