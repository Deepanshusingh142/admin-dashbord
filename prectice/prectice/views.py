#view ek trha se controller hai 
from django.http import HttpResponse   #ye lib http request ko response krti hai 
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password

from django.contrib.auth.decorators import login_required
# from .forms import usersForm 
from .models import usersignup



def home(request):
   
     user_id = request.session.get('user_id')
     user = usersignup.objects.get(id=user_id)
     totel_user = usersignup.objects.count()
    
     return render(request,"index.html",{
         'user':user,
         'totel_user':totel_user
         
     })




def add_customer(request):
    return render(request,"add-customer.html")

def forgot(request):
 
    user_id = request.session.get('user_id')
    if user_id:    
        user = usersignup.objects.get(id=user_id)
        return render(request,"forgot-password.html",{
            'user':user
        })  
    else:  
     return render(request,"forgot-password.html")

# login logic
def login(request):
   
    if request.method =="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        # request.session.modified = True   
        try:   
            # ab hum data ko nikalenge  user ka  db se mtb jo yaha object hai .get() se hum attribute pkdenge database ke
            user = usersignup.objects.get(email=email)
            
            if check_password(password,user.password):
                request.session['user_id']=user.id #isme 'user'=>varible hai aur id database me ek coloumn hai user.id smjhe fir kya hai
                request.session['user_email']=user.email
                # print("session set",request.session.items())
                return redirect("home")
            else:
                return render(request,"login.html",{"error":"Invalid password or Email"})
            
        except usersignup.DoesNotExist:  
            return render(request,"login.html",{"error":"User Does not exist"})
    return render(request,"login.html")

# end login

def logout(request):
    request.session.flush()
    return redirect('login')
    


def signup(request):
    try:
        if request.method=="POST":
       
            first = request.POST.get('first_name')
            last = request.POST.get('last_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            password = request.POST.get('password')
            confirm =request.POST.get('confirm')
            agree = request.POST.get('agree')
            if password != confirm:
                return render(request,"signup",{
                    "error":"password is not match check it " 
                    })
            hash_password = make_password(password)
            usersignup.objects.create(
                first_name = first,
                last_name = last,
                email = email,
                phone = phone ,
                password = hash_password
            )
            return redirect("login")
        else:
            return render(request,"signup.html")
    except:
        print("i thing this is the error plese cheak the program first  ")
    return render(request,"signup.html")









def error4(request,exception):
    return render(request,"404.html",status=404)



def error5(request):
    return render(request,"500.html")