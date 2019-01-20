from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #construct a dictionary to pass to the template engine as its contet
    #note the key boldmessage is the same as {{ boldmessage }} in the template
    context_dict = {'boldmessage': "Crunchy, ceamy, cookie, candy, cupcake!"}
    
    #return a rendered response to send to the client
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    context_dict = {'boldmessage':"Picture of a kitten and a puppy"}
    return render(request, 'rango/about.html', context=context_dict)
