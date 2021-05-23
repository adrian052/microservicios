from django.urls import path
from . import views


app_name = 'email'

urlpatterns = [
    path('send/',views.send_email, name='send')
]