from . import views
from django.urls import path

urlpatterns = [
    path('', views.home_page, name='home'),
    path('breakfast/', views.BreakfastList.as_view(), name='breakfast_list'),
    path('maincourse/', views.MainCourseList.as_view(), name='main_course_list'),
    path('soup/', views.SoupList.as_view(), name='soup_list'),
    path('appetizer/', views.AppetizerList.as_view(), name='appetizer_list'),
    path('sides/', views.SidesList.as_view(), name='sides_list'),
    path('dessert/', views.DessertList.as_view(), name='dessert_list'),
    path('search/', views.search_form, name='search_form')
]