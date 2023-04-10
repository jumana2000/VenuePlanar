from django.shortcuts import render, redirect
from Adminapp.models import *
from userapp.models import *
# Create your views here.

def managerindex(request):
    return render(request, 'managerindex.html')

def managerlogin(request):
    if request.method == "POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('password')
        if managerdb.objects.filter(name=username_r, password=password_r).exists():
            data = managerdb.objects.filter(name=username_r, password=password_r).values('venuename').first()
            request.session['manager_username'] = username_r
            request.session['venue'] = data['venuename']

            return redirect('managerindex')
        else:
            return render(request,'managerlogin.html',{'message':'Invalid user credentials'})

    else:
        return render(request,'managerlogin.html')
    
def view_booking(request):
    venue = request.session.get('venue')
    data = Booking.objects.filter(venue=venue)
    book = Booking.objects.filter(venue=venue).count()
    return render(request, 'view_booking.html', {'data':data,'book':book})

def managerlogout(request):
    del request.session['manager_username']
    del request.session['venue']
    return redirect('managerlogin')