from django.urls import path
from .views import *

urlpatterns = [
    path('1/', sa.as_view()),
    path('2/', s1a.as_view()),
    path('3/', s2a.as_view()),
]
