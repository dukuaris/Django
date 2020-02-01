from django.urls import path
from . import views
from visual.dash_apps.finished_apps import simpleexample

urlpatterns = [
    path('', views.visual, name='visual')
]
