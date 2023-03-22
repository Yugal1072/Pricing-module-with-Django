from django.db import models

# Create your models here.

class PricingConfig(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

class DistanceConfig(models.Model):
    pricing_config = models.ForeignKey(PricingConfig, on_delete=models.CASCADE)
    distance_upper_limit = models.FloatField()
    base_price = models.FloatField()
    additional_price_per_km = models.FloatField()

class TimeConfig(models.Model):
    pricing_config = models.ForeignKey(PricingConfig, on_delete=models.CASCADE)
    time_upper_limit = models.FloatField()
    multiplier_factor = models.FloatField()
