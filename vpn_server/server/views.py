import requests
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import UsersWebsite, WebsiteStatistics
from .forms import UserWebsiteForm


def home(request, page=1):
    return render(request, "server/index.html")


@login_required
def create_website(request):
    if request.method == 'POST':
        form = UserWebsiteForm(request.POST)
        if form.is_valid():
            website = form.save(commit=False)
            website.user = request.user
            website.save()
            return redirect('website_list')
    else:
        form = UserWebsiteForm()

    return render(request, 'create_website.html', {'form': form})


@login_required
def website_list(request):
    websites = UsersWebsite.objects.filter(user=request.user)
    return render(request, 'website_list.html', {'websites': websites})


@login_required
def website_statistics(request, website_id):
    website = UsersWebsite.objects.get(pk=website_id)
    statistics = WebsiteStatistics.objects.get(website=website)
    return render(request, 'website_statistics.html', {'website': website, 'statistics': statistics})


@login_required
def proxy_view(request, user_site_name, routes_on_original_site):
    try:
        website = UsersWebsite.objects.get(name=user_site_name, user=request.user)
    except UsersWebsite.DoesNotExist:
        return HttpResponse("The website was not found or you don`t have access to it.", status=404)

    proxy_url = f"localhost/{routes_on_original_site}"
    response = requests.get(proxy_url)
    content = response.text.replace(website.url, f"/{user_site_name}")

    return HttpResponse(content)
