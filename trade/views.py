from django.http import request
from django.shortcuts import render, redirect

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

def messagelist(request):
    return render(request, 'messagelist.html')

def messagelist (request):
    contact = Contact.objects.all()
    return render(request, 'messagelist.html', {'contact': contact})

def stk (request):
    return render(request, 'stk.html')

def checkout(request):
    product_id = request.GET.get('product_id')
    price = request.GET.get('price')

    if product_id and product_id  == "1":

     return render(request, 'checkout.html', {'product_id': product_id, 'price': price})