from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ItemViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('products', ItemViewSet)

urlpatterns = router.urls