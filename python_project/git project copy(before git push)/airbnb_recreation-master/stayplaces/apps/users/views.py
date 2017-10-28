from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
from models import User, Host
from ..locations.models import Place, Amenity
import bcrypt
import re

#------------------------ Page Loading --------------------------#


# Load home page
def index(request):
    places = Place.objects.all()
    if 'id' in request.session:
        #Get Logged in User
        user = User.objects.get(id = request.session['id'])
        
        #Check if logged in user is host
        if hasattr(user, 'host'):
            host = True
        else:
            host = False
        
        context = {
            'User': user,
            'Places': places,
            'Host': host,
        }
        return render(request , "users/index.html", context)

    else:
        return render(request , "users/index.html")

def listing(request, id):
    user = User.objects.get(id=id)
    if request.method == "POST":
        name = request.POST['name']
        place_type = request.POST['place_type']
        shared = request.POST['shared']
        rooms = request.POST['rooms']
        guests = request.POST['guests']
        beds = request.POST['beds']
        baths = request.POST['baths']
        private_bath = request.POST['private_bath']
        country = request.POST['country']
        street_address = request.POST['street_address']
        apt_number = request.POST['apt_number']
        city = request.POST['city']
        state = request.POST['state']
        zip = request.POST['zip']
        price = request.POST['price']
        amenities = request.POST.getlist('amenities')


        if private_bath == "Yes":
            private_bath = True
        else:
            private_bath = False

        if len(Host.objects.filter(user = user)) == 0:
            Host.objects.create(user = user)
            host = Host.objects.get(user = user)
        else:
            host = Host.objects.get(user = user)

        Place.objects.create(name=name, host=host, place_type=place_type, shared=shared, rooms=rooms, guests=guests,beds=beds, baths=baths, private_bath=private_bath, country=country, street_address=street_address, apt_number=apt_number, city=city, zip=zip, price=price)
        
        current_place = Place.objects.get(street_address = street_address)
        for a in amenities:
            Amenity.objects.create(name = a, place = current_place)

        return redirect("/")
            
    else:
        user = User.objects.get(id = request.session['id'])
        host = user.host
        #Check if logged in user is host
        if hasattr(user, 'host'):
            host_log = True
        else:
            host_log = False
        context = {
            'places': host.places.all(),
            'User': user,
            'Host': host_log
        }
        return render(request , 'users/listings.html', context)

def trips(request):
    user = User.objects.get(id = request.session['id'])
    #Check if logged in user is host
    if hasattr(user, 'host'):
        host_log = True
    else:
        host_log = False
    context = {
        'User': user,
        'Host': host_log
    }
    return render(request , 'users/trips.html', context)

def hosting(request): 
    if 'id' in request.session:
        user = User.objects.get(id = request.session['id'])

        #Check if logged in user is host
        if hasattr(user, 'host'):
            host_log = True
        else:
            host_log = False
        context = {
            'User': user,
            'Host': host_log 
        }
        return render(request , "users/host.html", context)
    else:
        return render(request , "users/host.html")

def profile(request, id): 
    if 'id' in request.session:
        user = User.objects.get(id = request.session['id'])
        profile = User.objects.get(id = id)
        places = Place.objects.filter(host = user.host)

        #Check if logged in user is host
        if hasattr(user, 'host'):
            host_log = True
        else:
            host_log = False

        #Check if profile user is host
        if hasattr(profile, 'host'):
            profile_host = True
        else:
            profile_host = False

        context = {
            'User': user,
            'Host': host_log,
            'Profile': profile,
            'Profile_host': profile_host ,
            'Places': places
        }
        return render(request , "users/profile.html", context)
    else:
        return render(request , "users/profile.html")

def edit_profile(request): 
    if 'id' in request.session:
        user = User.objects.get(id = request.session['id'])
        #Check if logged in user is host
        if hasattr(user, 'host'):
            host_log = True
        else:
            host_log = False

        context = {
            'User': user,
            'Host': host_log,
        }
        return render(request , "users/edit.html", context)
    else:
        return render(request , "users/edit.html")

def upload(request):
    user = User.objects.get(id = request.session['id'])
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        user.photo = myfile
        user.save
        return redirect('/')    

def edit(request, id):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    gender = request.POST['gender']
    email = request.POST['email']
    phone = request.POST['phone']
    location = request.POST['location']
    desc = request.POST['desc']
    


#------------------------ LOGIN CODE --------------------------#

def register(request):
    if request.method == "POST":
        #Validation in models.py AND creates user if no errors
        valid, response = User.objects.register_validator(request.POST)
        if valid:
            request.session['id'] = response.id
            return redirect('/')
        else:
            for message in response:
                messages.error(request, message)
            return redirect('/login')
    else:
        return redirect('/')

def login(request):
    if request.method == "POST":
        #Validation in models.py
        valid, response = User.objects.login_validator(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        if valid:
            request.session['id'] = response.id
            return redirect("/")
        else:
            for message in response:
                messages.error(request, message)
            return redirect('/login')
    else:
        context = {
        'Users': User.objects.all(),
    }
    return render(request , "users/login.html", context)
         
def logout(request):
    del request.session['id']
    return redirect("/")
