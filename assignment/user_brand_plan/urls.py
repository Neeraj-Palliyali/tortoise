from django.contrib import admin
from django.urls import path,include

from rest_framework.routers import DefaultRouter

from .views import UserBrandPlansViewset

router = DefaultRouter(trailing_slash = False)

router.register(r"plans", UserBrandPlansViewset, basename = 'plans')
urlpatterns = [
    path("api/", include(router.urls)),
]
