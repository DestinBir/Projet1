from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    
    return render(request, 'blog.html', {'name':'Destin', 'age':19})
