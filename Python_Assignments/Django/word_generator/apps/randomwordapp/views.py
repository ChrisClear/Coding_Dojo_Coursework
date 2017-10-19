from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    return render(request, 'randomwordapp/index.html')

def randomword(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1
    word = ''
    my_letters_and_numbers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
    
    for times in range (0, 14):
        word = word + str(random.choice(my_letters_and_numbers))
    words = {
        'random_word': word
    }
    return render(request, 'randomwordapp/index.html', words)

def reset(request):
    request.session.clear()
    return redirect('/')
