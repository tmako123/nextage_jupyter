from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.index, name='index'),
    path('multi_button', views.multi_button),
    path('more', views.more),
    path('ajax',views.ajax),
    path('ajax_get_json', views.ajax_get_json)
]