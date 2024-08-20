from django.shortcuts import render
from data.models import *
# Create your views here.
def home(request):
    result=Book.objects.all()
    return render(request,'home.html',{'books':result})


def BookV(request):
    if request.method=="POST":
        name=request.POST.get('bname')
        p=request.POST.get('price')
        g=request.POST.get('genre')
        s=request.POST.get('aid')
        if Author.objects.filter(id=s).exists():
            a=Author.objects.get(id=s)
            obj=Book(title=name,price=p,genre=g,author=a)
            obj.save()
    return render(request,'book.html')


def AuthorV(request):
    if request.method=="POST":
        name=request.POST.get('aname')
        age=request.POST.get('age')
        rating=request.POST.get('rate')
        print(name,age,rating)
        obj=Author(name=name,age=age,rate=rating)
        obj.save()
    return render(request,'author.html')
