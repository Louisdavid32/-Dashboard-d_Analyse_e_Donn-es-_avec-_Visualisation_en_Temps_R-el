from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SaleViewSet, ProductPerformanceViewSet, MarketTrendViewSet
from .views import chatbot

router = DefaultRouter()
router.register(r'sales', SaleViewSet)
router.register(r'product-performance', ProductPerformanceViewSet)
router.register(r'market-trends', MarketTrendViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/chatbot/', chatbot, name='chatbot'),
]


