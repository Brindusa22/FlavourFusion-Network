from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('breakfast/', views.breakfast_detail, name='breakfast_detail')
]