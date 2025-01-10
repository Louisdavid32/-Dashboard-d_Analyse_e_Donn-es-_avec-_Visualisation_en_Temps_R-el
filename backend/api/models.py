from django.db import models

class Sale(models.Model):
    product_name = models.CharField(max_length=255)
    amount = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name} - {self.amount}"

class ProductPerformance(models.Model):
    product_name = models.CharField(max_length=255)
    sales_volume = models.IntegerField()
    customer_rating = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.product_name} - {self.sales_volume} units"

class MarketTrend(models.Model):
    trend_name = models.CharField(max_length=255)
    value = models.FloatField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.trend_name} - {self.value}"