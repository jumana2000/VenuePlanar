
from django.urls import path
from.import views


urlpatterns = [
    path('venueadmin/',views.venueadmin,name='venueadmin'),
    path('venueform/',views.venueform,name='venueform'),
    path('getdata/',views.getdata,name='getdata'),
   
    path('viewVenue/',views.viewVenue,name='viewVenue'),
    path('delete/<int:id>/',views.delete, name='delete'),
    path('edit/<int:id>/',views.edit, name='edit'),
    path('editupdate/<int:id>/', views.editupdate, name='editupdate'),

    path('addservice/',views.addservice,name='addservice'),
    path('servicedata/',views.servicedata,name='servicedata'),
    path('viewservice/',views.viewservice,name='viewservice'),
    path('deleteservice/<int:id>/', views.deleteservice, name='deleteservice'),
    path('editservice/<int:id>/', views.editservice, name='editservice'),
    path('editserviceupdate/<int:id>/', views.editserviceupdate, name='editserviceupdate'),
    path('addmanager/', views.addmanager, name='addmanager'),
    path('viewmanager/', views.viewmanager, name='viewmanager'),
    path('managerdata/', views.managerdata, name='managerdata'),
    path('order/', views.order, name='order'),
    path('user/', views.user, name='user'),
    path('message/', views.message, name='message'),
    path('', views.adminlogin, name='adminlogin'),
    path('adminlogout/', views.adminlogout, name='adminlogout'),
    path('viewuser/', views.viewuser, name='viewuser'),
    path('viewbooking/', views.viewbooking, name='viewbooking'),        
]
