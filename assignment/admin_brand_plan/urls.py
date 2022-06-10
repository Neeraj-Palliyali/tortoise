from django.contrib import admin
from django.urls import path,include

from rest_framework.routers import DefaultRouter

from .views import AdminPlanViewset

router = DefaultRouter(trailing_slash = False)

router.register(r"plans", AdminPlanViewset, basename = 'plans')
urlpatterns = [
    path("api/", include(router.urls)),
]
