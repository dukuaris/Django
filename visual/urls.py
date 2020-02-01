from django.urls import path
from . import views
from visual.dash_apps.finished_apps import gapminder

urlpatterns = [

    path('', views.visual, name='index'),

    path('gapminder/', views.gapminder, name='gapminder'),
]
