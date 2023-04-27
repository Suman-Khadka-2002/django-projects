from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name':'Suman'})

def add(request):

    value1 = int(request.POST['num1'])  # Requesting num1 value, also by default value1 gets string value so converting to integer type
    value2 = int(request.POST['num2'])
    res = value1 + value2
    return render(request, 'result.html', {'result':res})