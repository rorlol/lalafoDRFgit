from django.urls import path, include
from rest_framework import routers
from .views import CategoryViewSet, ProductsViewSet

router = routers.DefaultRouter()
router.register('product/', ProductsViewSet)
router.register('category/', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls))
]