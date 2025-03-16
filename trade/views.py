from django.http import request,JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from trade.forms import ContactForm
from trade.models import Contact
import base64
import datetime
import requests
from django.conf import settings
from requests.auth import HTTPBasicAuth


# Create your views here.
def index(request):
    return render(request, 'index.html')
def pay(request):
    return render(request,'trade/pay.html')

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

def initiate_mpesa_payment(request):
    short_code = 174379
    lipa_na_mpesa_online_shortcode = '174379'
    lipa_na_mpesa_shortcode_key = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
    lipa_na_mpesa_shortcode_secret = 'aLJq2fcU8Gs2ARAsFBWri6RqSJtDFcedRNSpXpltqwxGg2qMFOXN62Z8KUYgL50h'
    lipa_na_mpesa_shortcode_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequests'
    phone_number = request.POST.get('phone_number')
    amount = request.POST.get('amount')
    headers = {
        'Authorization':'Bearer'+get_access_token(),
        'Content-Type':'application/json'
    }
    paylod = {
        'BusinessShortCode':lipa_na_mpesa_online_shortcode,
        'LipaNaMpesaOnlineShortcode':lipa_na_mpesa_online_shortcode,
        'LipaNaMpesaOnlineShortcodeKey':lipa_na_mpesa_shortcode_key,
        'PhoneNumber':phone_number,
        'Amount':amount,
        'Shortcode': lipa_na_mpesa_shortcode_key,
        'AccountReference':'Test123',
        'TransactionDesc':'Payment for services'

    }
    response = requests.post(lipa_na_mpesa_shortcode_url,json=paylod,headers=headers)
    if response.status_code == 200:
        return JsonResponse({'status':'success','data':response.json()})
    else:
        return JsonResponse({'status':'failure','error':response.text})

def get_access_token():
    consumer_key = 'qUU0naftLohLqhwaAF3e1k7OMySZuoepipccJv95xZ84zOpN'
    consumer_secret = 'aLJq2fcU8Gs2ARAsFBWri6RqSJtDFcedRNSpXpltqwxGg2qMFOXN62Z8KUYgL50h'
    api_url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentialls'
    auth = HTTPBasicAuth(consumer_key,consumer_secret)
    response = requests.get(api_url,auth=auth)
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        return None
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



