from django.contrib.auth import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('localhost/<str:user_site_name>/<path:routes_on_original_site>/', views.proxy_view, name='proxy_view'),
    path('users/', include('users.urls')),
]
