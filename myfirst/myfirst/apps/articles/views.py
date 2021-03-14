from django.http import  HttpResponse
from django.shortcuts import render

def main(request):
    return render(request, 'articles/furniture.html')

def index(request):
    return render(request, 'articles/shop.html')

def about(request):
    return render(request, 'articles/about-us.html')

def contact(request):
    return render(request, 'articles/contact-us.html')
