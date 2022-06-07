from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserBrandPlansViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        
        return Response( { "success" : "HEHE" })