from django.urls import path

from . import views

app_name = "consent"
urlpatterns = [
    path('', views.index, name='index')
]
