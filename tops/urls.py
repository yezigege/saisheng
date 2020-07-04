from django.urls import path

from . import views


app_name = 'tops'

urlpatterns = [
    path('upload', views.UploadView.as_view(), name='upload'),
    path('show', views.ShowView.as_view(), name='show'),
]
