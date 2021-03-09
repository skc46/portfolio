from django.shortcuts import render, get_object_or_404
from .models import ContactForm
from .forms import MessageForm
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.

def homepage(request):
    return render(request, 'portfolioapp/index.html', {})


# def about(request):
#     if request.method=="POST":
#         contact = ContactForm()
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         message = request.POST.get('message')
#         contact.Name=name
#         contact.Email = email
#         contact.Message = message
#         contact.save()
#         contact = ContactForm()
#         # if contact.is_valid(): 
#         #    contact.save()
#         #    contact = ContactForm()

#         return render(request, 'portfolioapp/about.html', {'name':name})

#     else:
#         return render(request, 'portfolioapp/about.html', {})   

def about(request):
    form = MessageForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = MessageForm()
        name = request.POST['Name']
        email = request.POST['Email']
        message = request.POSt['Message']
        
        # send email
        send_mail(
            name,
            email,
            message,
            ['pooja.kc3062@gmail.com'],
           )
        return render(request, 'portfolioapp/about.html', {'name':name})

    else:    

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
    return render(request, 'portfolioapp/gallery.html', {})       
