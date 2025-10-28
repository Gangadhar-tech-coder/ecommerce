from django.urls import path
from .views import login_view
from users import views as views

urlpatterns = [
    path('', views.login_view, name='login'),
]


