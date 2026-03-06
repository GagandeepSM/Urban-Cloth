from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from sweets.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "sweets/sweets.html", {'title' : 'Main Page'} )
 
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, desc=desc, phone=phone,date=datetime.today() )
        contact.save()
        messages.success(request, 'Profile details updated.')

    return render(request, "sweets/contact.html", {'title' : '/Contact Page'})
    # return HttpResponse("Hey I am Contact!")

def products(request):
    return render(request, "sweets/products.html", {'title' : 'products'} )
