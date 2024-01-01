from django.shortcuts import render
from . forms import contactForm, inputForm 
# Create your views here.
def home(request):
    return render(request, './formapp/home.html')
    
def about(request):
        return render(request, './formapp/about.html')
        
  
def DjangoForm(request):
        form = contactForm()
        return render(request, './formapp/form.html', {'form':form}) 


def InputForm(request):
       form = inputForm()
       return render(request, './formapp/form.html', {'form':form}) 