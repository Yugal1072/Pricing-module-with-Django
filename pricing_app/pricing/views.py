from django.shortcuts import render
from .models import PricingConfig, DistanceConfig, TimeConfig

# Create your views here.

def index(request):
    active_configs = PricingConfig.objects.filter(is_active=True)
    return render(request, 'index.html', {'active_configs': active_configs})

def calculate_invoice(request):
    distance = float(request.POST['distance'])
    time = float(request.POST['time'])

    active_configs = PricingConfig.objects.filter(is_active=True)
    total_cost = 0

    for config in active_configs:
        distance_configs = DistanceConfig.objects.filter(pricing_config=config, distance_upper_limit__gte=distance).order_by('distance_upper_limit').first()
        time_configs = TimeConfig.objects.filter(pricing_config=config, time_upper_limit__gte=time).order_by('time_upper_limit').first()

        if distance_configs and time_configs:
            base_price = distance_configs.base_price
            additional_price_per_km = distance_configs.additional_price_per_km
            multiplier_factor = time_configs.multiplier_factor

            total_cost += base_price + (additional_price_per_km * distance) * multiplier_factor
            # print("Total Cost of the Distance travel is: ",total_cost)

    return render(request, 'invoice.html', {'total_cost': total_cost})
