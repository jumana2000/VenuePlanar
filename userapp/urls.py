from django.urls import path,include
from.import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('details/<int:id>/',views.details,name='details'),
    path('venues/',views.venues,name='venues'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('contactdata/', views.contactdata, name='contactdata'),
    path('bookdata/<int:id>/', views.bookdata, name='bookdata'),
    path('checkout/', views.checkout, name='checkout'),
    path('confirmorder/<int:bookid>/', views.confirmorder, name='confirmorder'),
    path('register/', views.register, name='register'),
    path('registerdata/', views.registerdata, name='registerdata'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('userlogout/', views.userlogout, name='userlogout')
    
]