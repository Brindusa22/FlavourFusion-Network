from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('breakfast/', views.BreakfastList.as_view(), name='breakfast_detail'),
    path('maincourse/', views.MainCourseList.as_view(), name='main_course_list')
]