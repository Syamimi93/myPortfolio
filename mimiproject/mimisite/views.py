from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import ContactForm
 
def index(request):
    return render(request, 'index.html', {})

def portfolio(request):
    return render(request, 'portfolio.html', {})

def contact(request):
    print('skrg kat sini')
    if request.method == 'POST':
        
        name = request.POST['name']
        email = request.POST['email']
        msg = request.POST['msg']
        print('sampai sini dah')

        save_data = ContactForm()
        save_data.name = name
        save_data.email = email
        save_data.message = msg
        save_data.save()
    else:
        return render (request,"contact.html")
    
    return render (request,"contact.html")




