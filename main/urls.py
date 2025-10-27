from django.urls import path,include
from .views import *
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
    # path('ecommerce/',views.main_view,name='main'),
    path('', views.home, name='home'),
    path('settings/', views.settings, name='settings'),
    path('orders/', views.orders, name='orders'),
    path('products/', views.products, name='products'),
    path('customers/', views.customers, name='customers'),
    path('login/',auth_views.LoginView.as_view(template_name='views/login.html'), name='login'),
]