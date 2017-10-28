from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from .. users.models import User
from models import Place
import bcrypt
import re

#------------------------ LOGIN CODE --------------------------#
# Load home page
def index(request):
    if 'id' in request.session:
        user = User.objects.get(id = request.session['id'])
        places = Place.objects.all()
        
        context = {
            'User': user, 
            'places': places,
        }
        return render(request , "locations/index.html", context)
    else:
        return render(request , "locations/index.html")

def show(request, id):
    if 'id' in request.session:
        user = User.objects.get(id = request.session['id'])
        place = Place.objects.get(id = id)
        print place.host.user.id
        amenities = place.amenities.all()
        context = {
            'User': user, 
            'place': place,
            'amenities': amenities
        }
        return render(request , "locations/show.html", context)