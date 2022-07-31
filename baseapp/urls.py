import imp
from  django.urls import path
from . import views
 
urlpatterns= [
    path('',views.home,name="home"),
    # Sending the dynamic value
    path('room/<str:pk>',views.rooms,name="room"),
    path('show/',views.show,name="show"),
    path('updateroom/<str:pk>',views.updateroom,name="updateroom"),
    path('deleteroom/<str:pk>',views.deleteroom,name="deleteroom"),

]