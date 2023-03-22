from django.contrib import admin
from .models import DistanceConfig, TimeConfig, PricingConfig

# Register your models here.

# class DistanceConfigAdmin(admin.ModelAdmin):
#     list_display = ('distance_upper_limit', 'base_price', 'additional_price_per_km')

# class TimeConfigAdmin(admin.ModelAdmin):
#     list_display = ('time_upper_limit', 'multiplier_factor')

# class PricingConfigAdmin(admin.ModelAdmin):
#     list_display = ('name', 'is_active')
#     filter_horizontal = ('distance_config', 'time_config')

admin.site.register(DistanceConfig)
admin.site.register(TimeConfig)
admin.site.register(PricingConfig)

