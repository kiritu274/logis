from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
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
