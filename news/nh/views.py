from django.shortcuts import render, HttpResponse
from .models import Articles

# print(details)
def display(request):
    details = Articles.objects.all()
    context = {
        'article' : details
    }
    return render(request,'index.html', context)

def about_me(request):
    details = Articles.objects.all()
    context = {
        'article' : details
    }
    return render(request,'about_me.html', context)

def display1(request,pk):
    data1 = Articles.objects.get(id = pk)
    context = {
        'data1':data1
    }
    return render(request,'display.html',context)