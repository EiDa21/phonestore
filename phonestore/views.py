from django.shortcuts import render
 
def home(request):
        return render(request, 'phonestore/index.html', {})
    
def about(request):
      return render(request, 'phonestore/about.html', {})

def computer(request):
      return render(request, 'phonestore/computer.html', {})

def laptop(request):
      return render(request, 'phonestore/laptop.html', {})

def product(request):
      return render(request, 'phonestore/product.html', {})

def contact(request):
      return render(request, 'phonestore/contact.html', {})
# Create your views here.
