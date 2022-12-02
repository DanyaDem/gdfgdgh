from django.shortcuts import render
from django.shortcuts import HttpResponse

def index(request):
    return render(request,'index.html')

def load(request):
    name= request.POST.get('name', 'asfafasf')
    email= request.POST.get('email', 'asfafasf')
    phone= request.POST.get('phone', 'asfafasf')
    service= request.POST.get('service', 'asfafasf')
    return HttpResponse(f'{name},<br> {email},<br> {phone},<br> {service},<br>')

