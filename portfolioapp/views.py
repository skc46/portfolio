from django.shortcuts import render, get_object_or_404
from .models import ContactForm
from .forms import MessageForm
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request, 'portfolioapp/index.html', {})


""" def about(request):
    if request.method=="POST":
        contact = ContactForm()
        name=request.POST.get('name')
        email=request.POST.get('email')
        message = request.POST.get('message')
        contact.Name=name
        contact.Email = email
        contact.Message = message
        if contact.is_valid(): 
           contact.save()
           contact = ContactForm()
 """
        #return HttpResponse("<h1>Thanks for sending your message!</h1>")
def about(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = MessageForm()

    context = {
        'form' : form
    }    
    return render(request, 'portfolioapp/about.html', context)

def resume(request):
    return render(request, 'portfolioapp/resume.html', {})

def research(request):
    return render(request, 'portfolioapp/research.html', {})   

def publication(request):
    return render(request, 'portfolioapp/publications.html', {}) 

def presentation(request):
    return render(request, 'portfolioapp/presentation.html', {}) 
      
def resource(request):
    return render(request, 'portfolioapp/coding.html', {})  

def gallery(request):
    return render(request, 'portfolioapp/base.html', {})       
