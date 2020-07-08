from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('slam', views.slam, name='index'),
    path('postPose', views.postPose, name='index'),
]