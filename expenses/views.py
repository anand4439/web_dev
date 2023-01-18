from django.shortcuts import render,redirect
# from urllib import request

# Create your views here.

def index(request):
    return render(request,'expenses/index.html')

def add_expenses(request):
    return render(request,'expenses/add_expenses.html')    

