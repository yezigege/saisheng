from django.urls import path

from . import views

app_name = 'tops'

urlpatterns = [
    path('', views.HelloView.as_view(), name='hello')
]
