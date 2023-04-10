from django.shortcuts import render, redirect
from django.http import HttpResponse
from. models import *
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from userapp.models import *

# Create your views here.

def venueadmin(request):
    venuecount = Venuedb.objects.all().count()
    usercount = Register.objects.all().count()
    ordercount = Confirmation.objects.all().count()
    return render(request,'venueadmin.html',{'venuecount':venuecount,'usercount':usercount,'ordercount':ordercount})

def venueform(request):
    data = Servicedb.objects.all()
    manager = managerdb.objects.all()
    return render(request,'form.html',{'data':data,'manager':manager})

def getdata(request):
    if request.method=="POST":
        venue_name=request.POST.get('vname')
        address=request.POST.get('address')
        manager=request.POST.get('manager')
        description=request.POST.get('vdesc')
        price=request.POST.get('price')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        venue_img=request.FILES['image']
        data=Venuedb(venue_name=venue_name,address=address,manager=manager,description=description,
        price=price,phone=phone,email=email,venue_img=venue_img)
        data.save()
    return redirect('viewVenue')


def viewVenue(request):
    data=Venuedb.objects.all()
    return render(request,'viewvenue.html',{'data':data})


def delete(request,id):
    Venuedb.objects.filter(id=id).delete()
    return redirect('viewVenue')

def edit(request,id):
    data=Venuedb.objects.filter(id=id)
    service = Servicedb.objects.all()
    return render(request,'edit.html',{'data':data,'service':service})

def editupdate(request,id):
    if request.method == 'POST':
        name_c = request.POST.get('vname')
        address_c = request.POST.get('address')
        man_c=request.POST.get('manager')
        vdesc_c=request.POST.get('vdesc')
        price_c=request.POST.get('price')
        phone_c=request.POST.get('phone')
        email_c=request.POST.get('email')
        
        try:
            img_c = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img_c.name, img_c)
        except MultiValueDictKeyError:
            file = Venuedb.objects.get(id=id).venue_img
            Venuedb.objects.filter(id=id).update(venue_name=name_c,address=address_c,manager=man_c,description=vdesc_c,
                price=price_c,phone=phone_c,email=email_c,venue_img=file)
    return redirect('viewVenue')   

def addservice(request):
    return render(request,'addservice.html')

def servicedata(request):
    if request.method=="POST":
        sname=request.POST.get('sname')
        cost=request.POST.get('cost')
        service_image=request.FILES['simage']
        data=Servicedb(sname=sname,cost=cost,service_image=service_image)
        data.save()
    return redirect('viewservice')

def viewservice(request):
    data=Servicedb.objects.all()
    return render(request,'viewService.html',{'data':data})    

def deleteservice(request,id):
    Servicedb.objects.filter(id=id).delete()
    return redirect('viewservice')

def editservice(request,id):
    data=Servicedb.objects.filter(id=id)
    return render(request,'editservice.html',{'data':data})

def editserviceupdate(request,id):
    if request.method=="POST":
        name_u=request.POST.get('sname')
        cost_u=request.POST.get('cost')
       
        try:
            image_u = request.FILES['simage']
            fs = FileSystemStorage()
            file = fs.save(image_u.name, image_u)
        except MultiValueDictKeyError:
            file = Servicedb.objects.get(id=id).service_image
            Servicedb.objects.filter(id=id).update(sname=name_u,cost=cost_u,service_image=file)
    return redirect('viewservice')   


def addmanager(request):
    data = Venuedb.objects.all()
    return render(request, 'addmanager.html',{'data':data})

def viewmanager(request):
    data = managerdb.objects.all()
    return render(request, 'viewmanager.html',{'data':data})

def managerdata(request):
    if request.method == "POST":
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        venuename = request.POST.get('venuename')
        email = request.POST.get('email')
        password = request.POST.get('password')
        image = request.FILES['mimage']

        data = managerdb(name=name, address=address, phone=phone, venuename=venuename,email=email, password=password, image=image)
        data.save()
        return redirect('viewmanager')


def order(request):
    data = Confirmation.objects.all()
    return render(request,'order.html',{'data':data})
           
def user(request):
    data = Register.objects.all()
    return render(request, 'user.html', {'data':data})

def message(request):
    data = Contactdb.objects.all()
    return render(request,'message.html',{'data':data})

def adminlogin(request):
    if request.method == "POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')
        user = authenticate(username=username_r, password=password_r)
        if user is not None:
            login(request,user)
            request.session['username_a'] = username_r
            request.session['password_a'] = password_r
            return redirect('venueadmin')
        else:
            return render(request, 'adminlogin.html',{'message':'Sorry, Invalid user credentials'})
    else:
        return render(request, 'adminlogin.html')

def adminlogout(request):
    del request.session['username_a']
    del request.session['password_a'] 
    return redirect('adminlogin')

def viewuser(request):
    data=Register.objects.all()
    return render(request,'viewuser.html',{'data':data})    

def viewbooking(request):
    data=Booking.objects.all()
    return render(request,'viewbooking.html',{'data':data})        