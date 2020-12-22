from django.urls import path

from . import views

urlpatterns = [
    path('settings/', views.settings, name='settings'),
    path('profile/', views.profile, name='profile'),
    path('calendar/', views.calendar, name='calendar'),
]