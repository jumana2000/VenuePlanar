
from django.urls import path
from.import views


urlpatterns = [
    path('managerindex/',views.managerindex,name='managerindex'),
    path('managerlogin/',views.managerlogin,name='managerlogin'),
    path('view_booking/',views.view_booking,name='view_booking'),
    path('managerlogout/', views.managerlogout, name='managerlogout')
]