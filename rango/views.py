from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #construct a dictionary to pass to the template engine as its contet
    #note the key boldmessage is the same as {{ boldmessage }} in the template
 #   context_dict = {'boldmessage': "Crunchy, ceamy, cookie, candy, cupcake!"}
    return HttpResponse("Rango says hey there partner! <br/> <a href='about/'>About</a>")
    #return a rendered response to send to the client
#    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("Rango says here is the about page. <br/> <a  href'/rango/'>Index</a>")
 #   context_dict = {'boldmessage':""}
  #  return render(request, 'rango/about.html', context=context_dict)



