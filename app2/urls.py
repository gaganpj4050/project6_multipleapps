from django.urls import path
from app2.views import *
app_name='nothing'
urlpatterns=[
    path('virat/',virat,name='virat'),
    path('abd/',abd,name='abd'),
]