from django.urls import path
from . import views
from visual.dash_apps.finished_apps import gapminder
from visual.dash_apps.finished_apps import multipleoutputs
from visual.dash_apps.finished_apps import interactions
from visual.dash_apps.finished_apps import stockprice

urlpatterns = [

    path('', views.visual, name='visualindex'),

    path('gapminder/', views.gapminder, name='gapminder'),

    path('multipleoutputs/', views.multipleoutputs, name='multipleoutputs'),

    path('interactions/', views.interactions, name='interactions'),

    path('stockprice/', views.stockprice, name='stockprice'),
]
