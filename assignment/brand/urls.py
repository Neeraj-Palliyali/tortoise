from django.urls import path,include

from rest_framework.routers import DefaultRouter

from .views import BrandPlanViewset

router = DefaultRouter(trailing_slash = False)

router.register(r"plans", BrandPlanViewset, basename = 'plans')
urlpatterns = [
    path("api/", include(router.urls)),
]
