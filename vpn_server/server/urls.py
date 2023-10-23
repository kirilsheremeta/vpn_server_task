from django.urls import path
from . import views

app_name = "server"

urlpatterns = [
    path('', views.home, name='home'),
    path('create-website/', views.create_website, name='create_website'),
    path('website-list/', views.website_list, name='website_list'),
    path('website-statistics/<int:website_id>/', views.website_statistics, name='website_statistics'),
    path('<str:user_site_name>/<path:routes_on_original_site>/', views.proxy_view, name='proxy_view'),
]
