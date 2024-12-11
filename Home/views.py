from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    context = {'nom':'Ulrich'}
    return render(request,"home/index.html", context)

def contact(request):
    return render(request, "home/contact.html")