from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def my_index(request):
    return render(request, template_name='detail/index.html')

def my_detail(request):
    return render(request, template_name='detail/detail.html')

def my_contract(request):
    return render(request, template_name='detail/contract.html')