from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.img = 'destination_1.jpg'
    dest1.name = "Kathmandu"
    dest1.desc = "Capital city"
    dest1.price = 700
    dest1.offer = False

    dest2 = Destination()
    dest2.img = 'destination_2.jpg'
    dest2.name = "Pokhara"
    dest2.desc = "City of lakes and ponds"
    dest2.price = 1500
    dest2.offer = True

    dest3 = Destination()
    dest3.img = 'destination_3.jpg'
    dest3.name = "Illam"
    dest3.desc = "City famous for the tea leaves"
    dest3.price = 1000
    dest3.offer = False

    dests = [dest1, dest2, dest3]

    return render(request, "index.html", {'dests': dests})