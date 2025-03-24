from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import AccessLog
from django.contrib.auth.decorators import login_required

def track(request):
    # Obter o IP do visitante
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    
    # Obter informações de geolocalização
    geo_data = {}
    if ip and ip != '127.0.0.1':  # Ignorar localhost para testes
        try:
            response = requests.get(f'http://ip-api.com/json/{ip}?fields=status,message,country,regionName,city,lat,lon,isp')
            geo_data = response.json()
        except:
            pass
    
    # Salvar no banco de dados
    log_entry = AccessLog(
        ip_address=ip,
        country=geo_data.get('country'),
        region=geo_data.get('regionName'),
        city=geo_data.get('city'),
        latitude=geo_data.get('lat'),
        longitude=geo_data.get('lon'),
        isp=geo_data.get('isp'),
        user_agent=request.META.get('HTTP_USER_AGENT')
    )
    log_entry.save()
    
    # Redirecionar para uma página normal
    return render(request, 'location/redirect_page.html')



@login_required
def view_logs(request):
    logs = AccessLog.objects.all().order_by('-access_time')
    return render(request, 'location/logs.html', {'logs': logs})