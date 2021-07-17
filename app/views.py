
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from.models import Buy
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password=request.POST['password']
        username=request.POST['username']
        user=User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)
        user.save();
        return redirect('/login')
    else:  
        return render(request,'register.html')

def home(request):
    return render(request,'home.html')
def login(request):
        if request.method=='POST':
            username=request.POST['username']
            password=request.POST['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect("/")
            else:
                messages.info(request,'invalid credentials')
                return redirect("/login")

        else:
            return render(request,'login.html')
def logout(request):

    auth.logout(request)
    return redirect("/home")
    # return render(request,'home.html')
# def buy(request):
#     if request.method=='POST':
#         item=request.POST['item']
#         quantity=request.POST['quantity']
#         phonenumber=request.POST['phonenumber']
#         username=request.POST['username']
#         if len(phonenumber)==10:
#             buy=Buy(item=item,quantity=quantity,phonenumber=phonenumber,status="Not Completed",username=username)
#             buy.save();
#             return redirect("/home")
#         else:
#             messages.info(request,'enter 10 digit phone number')
#             return redirect("/buy")

#     else:
        
#         return render(request,'buy.html')

def makeadeal(request):
    return render(request,'makeadeal.html')
def orders(request):
    order=Buy.objects.all()
    # x=User.first_name
# {{user.first_name}}
    return render(request,"orders.html",{'order':order})

def buy1(request):
        if request.method=='POST':
            item1=request.POST['item1']
            item1_quantity=request.POST['item1_quantity']
            username=request.POST['username']
            buy=Buy(item=item1,quantity=item1_quantity,status="Not Completed",username=username)
            buy.save();
            return redirect("/home")
        else:
            return render(request,"home.html")
# def buy2(request):
#     return render(request,'buy.html',{'name':'vennela  Icream'})
# def buy3(request):
#     return render(request,'buy.html',{'name':'Butterscotch Icream'})
# def buy4(request):
#     return render(request,'buy.html',{'name':'All mix Icream'})