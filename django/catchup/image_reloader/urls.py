from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('next_img', views.next_img, name='next_img'),
]