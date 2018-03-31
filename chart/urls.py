from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('draw_new/', views.draw_new),
    path('detail/<int:chart_id>/', views.chart_detail),
    path('', views.chart_list),
]
