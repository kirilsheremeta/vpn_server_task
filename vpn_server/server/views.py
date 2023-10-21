import django

import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import VPNStat


def home(request):
    return HttpResponse("Welcome to the Server!")


@login_required
def proxy_view(request, user_site_name, routes_on_original_site):
    original_site_url = f"https://localhost/{routes_on_original_site}"
    user = request.user
    response = requests.get(original_site_url)
    content = response.text
    content = content.replace('href="/', f'href="/localhost/{user_site_name}/')
    vpn_stat = VPNStat(user=user, site_url=original_site_url, data_sent=len(request.body),
                       data_received=len(response.content))
    vpn_stat.save()
    return HttpResponse(content)


@login_required
def user_stats(request):
    user = request.user
    stats = VPNStat.objects.filter(user=user)

    return render(request, 'user_stats.html', {'stats': stats})
