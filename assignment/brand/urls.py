from django.urls import path,include

from rest_framework.routers import DefaultRouter

from .views import BrandPlanViewset, PromotionViewset

router = DefaultRouter(trailing_slash = False)

router.register(r"plans", BrandPlanViewset, basename = 'plans')
router.register(r"promotion", PromotionViewset, basename = 'rpomotion')
urlpatterns = [
    path("api/", include(router.urls)),
]
