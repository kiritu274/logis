from django.http import request
from django.shortcuts import render, redirect, get_object_or_404

from trade.forms import ContactForm
from trade.models import Contact


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(contact)
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def services(request):
    return render(request, 'services.html')

def pricing(request):
    return render(request, 'pricing.html')

def services_details(request):
    return render(request, 'services_details.html')

def starter_page(request):
    return render(request, 'starter-page.html')

def get_a_quote(request):
    return render(request, 'get-a-quote.html')



def contactlist (request):
    contact = Contact.objects.all()
    return render(request, 'contactlist.html', {'contact': contact})


def updatecontact(request,id):
    message = get_object_or_404(Contact, id=id)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contactlist')
    else:
        form = ContactForm(instance = message)
    return render(request, 'update-contact.html', {'form': form})



def deletecontact(request,id):
    message = get_object_or_404(Contact, id=id)
    try:
        message.delete()
    except Exception as e:
        message.error(request, 'contact not deleted')
    return redirect('contactlist')



