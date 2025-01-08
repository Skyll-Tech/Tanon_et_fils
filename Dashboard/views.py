from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def test(request):
    return HttpResponse("Bonjourr")

def dashboard(request):
    return render(request, "dashboard/index.html")
