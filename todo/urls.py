
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [

    path('vonly/', views.TodoVueOnlyTV.as_view(), name='vonly'),

    path('create/', views.TodoCV.as_view(), name='create'),

    path('list/', views.TodoLV.as_view(), name='list'),

    #pathconvert 숫자가 들어오면 url로 변환
    path('<int:pk>/delete/', views.TodoDelV.as_view(), name='delete')
]
