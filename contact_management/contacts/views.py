from django.shortcuts import render,redirect
from .models import contacts


def home(request):
    return render(request,'home.html')

def add(request):
    if request.method=='POST':
        name=request.POST.get("name")
        pnumber=request.POST.get("number")
        email=request.POST.get("email")
        addrs=request.POST.get("address")
        contacts.objects.create(name=name,phone=pnumber,email=email,address=addrs)
        return redirect('/')
    else:
        return render(request,'adding.html')

def delete(request):
    if request.method=='POST':
        name=request.POST.get("name")
        if contacts.objects.filter(name=name).exists():
            d=contacts.objects.filter(name=name)
            d.delete()
            return redirect('/')
        else:
            return render(request,'deleting.html',{'msg':'contact list empty or contact with this name is not available please enter valid name or go to home'})
    else:
        return render(request,'deleting.html')
    
def search(request):
    if request.method=='POST':
        name=request.POST.get("name")
        if contacts.objects.filter(name=name).exists():
            c=contacts.objects.filter(name=name)
            dict={'contact':c,'name':'Name ->','phone':'Phone number ->','email':'Email ->','address':'Address ->'}
            return render(request,'searching.html',dict)
        else:
            return render(request,'searching.html',{'msg':'contact list empty or contact with this name is not available please enter valid name or go to home'})

        
    else:
        return render(request,'searching.html')

def view(request):
        if contacts.objects.all().exists():
            c=contacts.objects.all()
            dict={'contact':c,'name':'Name ->','phone':'Phone number ->','email':'Email ->','address':'Address ->'}
            return render(request,'viewing.html',dict)
        else:
            return render(request,'viewing.html',{'msg':'contact list empty'})
        