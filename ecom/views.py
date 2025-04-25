from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def product_detail(request):
    return render(request, 'product-detail.html')

