from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('chart_list/', views.chart_list, name='chart_list'),
    path('question/<int:chart_id>/', views.question, name='question'),
    path('create_chart/', views.create_chart, name='create_chart'),
    path('edit_chart/<int:chart_id>/', views.edit_chart, name='edit_chart'),
    path('delete_chart/<int:chart_id>/', views.delete_chart, name='delete_chart'),
    path('get_chart/<int:chart_id>/', views.get_chart, name='get_chart'),
]
