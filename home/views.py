from django.http import HttpRequest
from ast import Return
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect

from home.forms import BookingForm
from .models import Departments,Doctors

# Create your views here.
def index(request):
    return render(request, 'index.html')
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request,'confirmation.html')
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request, 'booking.html',dict_form)
def confirmation(request):
    return render(request, 'confirmation.html')
def doctors(request):
    dict_docs ={
        'doctors':Doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)
def department(request):
    dict_dep={
        'depart': Departments.objects.all()
    }
    return render(request, 'department.html',dict_dep)