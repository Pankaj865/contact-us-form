from django.shortcuts import render,redirect
from .models import Contact
from django.http import HttpResponse
# Create your views here.
def success(request):
    return render(request, "success.html" )

def index(request):
    if request.method == 'POST':
        contact=Contact()
        name=request.POST.get('fname')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        message=request.POST.get('message')
        contact.name=name
        contact.phone=phone
        contact.email=email
        contact.message=message
        contact.save()
        # return HttpResponse("welcome")
        return redirect('success')
    return render(request,'index.html')

