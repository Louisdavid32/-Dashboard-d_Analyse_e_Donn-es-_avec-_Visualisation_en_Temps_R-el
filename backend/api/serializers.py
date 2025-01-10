from rest_framework import serializers
from .models import Sale, ProductPerformance, MarketTrend

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

class ProductPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPerformance
        fields = '__all__'

class MarketTrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarketTrend
        fields = '__all__'