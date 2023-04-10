from django.shortcuts import render, redirect
from Adminapp.models import Venuedb
from . models import *
from django.http import HttpResponse
from django.db.models.aggregates import Sum

# Create your views here.

def home(request):
     data=Venuedb.objects.all()
     return render (request,'home.html',{'data':data})

def details(request,id):
     data=Venuedb.objects.filter(id=id)  
     service = Servicedb.objects.all()
     return render(request,'details.html',{'data':data,'service':service})

def venues(request):
     data=Venuedb.objects.all()
     return render(request,'venues.html',{'data':data})

def about(request):
    return render (request,'about.html')                    

def contact(request):
    return render (request,'contact.html')    

def contactdata(request):
     if request.method == "POST":
          name = request.POST.get('name')
          email = request.POST.get('email')
          message = request.POST.get('message')

          data = Contactdb(name=name, c_email=email, message=message)
          data.save()
          return redirect('home')
     
def bookdata(request, id):
     if 'id' in request.session:
          userid = request.session.get('id')
          date_time = request.POST.get('date_time')
          purpose = request.POST.get('purpose')
          services=request.POST.getlist('scales')
          venueid=request.POST.get('venueid')
          venue = request.POST.get('venue')
          service_name = request.POST.getlist('service')
          total=0
          for ele in range(0, len(services)):
               total = total + int(services[ele])
          total =int(total)
          print(type(total))
          venue_price = int(request.POST.get('venue_price'))
          print(type(venue_price))
          totalcost = venue_price+total
          
          if Booking.objects.filter(date_time=date_time,venueid=Venuedb.objects.get(id=id)).exists():
               return render(request,'checkout.html',{'error':'Sorry already booked'})
          else:
               data = Booking(venue=venue,venueid=Venuedb.objects.get(id=id),userid=Register.objects.get(id=userid),date_time=date_time,purpose=purpose,selected_service=services,service_name=service_name,total=totalcost)
               data.save()
               
               return redirect('checkout')       

          #data = Booking(total=totalcost,service_name=service_name,venueid=Venuedb.objects.get(id=id),userid=Register.objects.get(id=userid),selected_service=services,date_time=date_time,purpose=purpose, service_amount=total)     
          #data.save()
          #return redirect('checkout')
     else:
          return render(request, 'details.html', {'message':'Please Login'})


def checkout(request):
     userid = request.session.get('id')
     data = Booking.objects.filter(status=0,userid=userid)
     return render(request, 'checkout.html',{'data':data})

def confirmorder(request, bookid):
     if request.method == "POST":
          userid = request.session.get('id')
          data = Confirmation(userid=Register.objects.get(id=userid), bookingid=Booking.objects.get(id=bookid))
          data.save()
          Booking.objects.filter(id=bookid).update(status=1)

          return render(request, 'checkout.html',{'message':'Thank you, Successfully Booked'})
     
     
def register(request):
     return render(request, 'register.html')    

def registerdata(request):
     if request.method == "POST":
          username = request.POST.get('username')
          password = request.POST.get('password')
          email = request.POST.get('email')
          phone = request.POST.get('phone')

          data = Register(username=username, password=password, email=email, phone=phone)
          data.save()
          return redirect('home')
     
def userlogin(request):
     if request.method == "POST":
          username = request.POST.get('username')
          password = request.POST.get('password')
          if Register.objects.filter(username=username, password=password).exists():
               data = Register.objects.filter(username=username, password=password).values('id','phone','email','id').first()
               request.session['username'] = username
               request.session['password'] = password
               request.session['phone'] = data['phone']
               request.session['email'] = data['email']
               request.session['id'] = data['id']

               return redirect('home')
          
          else:
               return render(request,'userlogin.html',{'message':"Sorry, Invalid user credentials"})
     
     else:
          return render(request, 'userlogin.html')


def userlogout(request):
     del request.session['username']
     del request.session['password']
     del request.session['phone']
     del request.session['email']
     del request.session['id'] 
     return redirect('home')