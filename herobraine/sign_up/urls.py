from django.urls import path
from . import views

app_name = 'sign_up'
urlpatterns = [
    
    path('', views.index, name='index'),
    path('<str:username>/status', views.status, name = 'status'),
    path('form', views.form, name='form'),
]
