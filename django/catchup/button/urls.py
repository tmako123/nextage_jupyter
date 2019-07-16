from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('multi_button', views.multi_button),
    path('more', views.more),
    path('ajax',views.ajax),
    path('json_post', views.json_receive),
    path('json_get', views.json_send)
]