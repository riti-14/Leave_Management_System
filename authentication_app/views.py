from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,login


# Create your views here.

def createUserView(request):
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirmpassword']
        if password == confirm_password:
            if User.objects.filter(username = username).exists():
                messages.error(request,'Username already exist')
                return render(request,'user_register.html')
            elif User.objects.filter(email = email).exists():
                messages.error(request,'email already exist')
                return render(request,'user_register.html')
            else:
                user=User.objects.create_user(first_name = first_name,last_name = last_name,username = username,email=email,password = password)
                user.save()
                # return HttpResponse('user create')
                return redirect('login')
        else:
            messages.error(request,'password does not match')
            return render(request,'user_register.html')
    else: 
        return render(request,'user_register.html')
    


def loginUserView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username,password = password)
        if user is not None:
            # if request.user.is_superuser ==
                login(request,user)
                    # return redirect('/manage')
                return render(request,'demo.html')
            # else:
                # login(request,user)
                # return redirect('home')

        else:
            messages.error(request,'Invalid Credentials')
            return render(request,'user_login.html')
    else:
        return render(request,'user_login.html')














































































# def demoView(request):
   
#     return render(request,'demo.html')



# def createUserView(request):
#     user_type_choices=createUserModel.objects.all() 
#     userchoices = createUserModel.userchoices    
                 
#     context={
#             "user_type_choices" : user_type_choices,
#             'user_type_choices':userchoices
#             }
    
#     if request.method == 'POST':
        
#         name = request.POST["name"]
#         email =  request.POST["email"]
#         number=  request.POST["number"]
#         password=  request.POST["password"]
#         select_value=request.POST['select_value']


#         register=createUserModel(name=name,email=email,number=number,password=password,user_type=select_value)
#         register.save()
#         return redirect('login')
    
#     return render(request,'user_register.html',context)


# def loginUserView(request):
#     if request.method == 'POST':
#         email_id=request.POST['email_id']
#         password=request.POST['password']
        
#         user=authenticate(username="ashok",password=password)
#         if user is not None:
#             login(request,user)
#             return render(request,'demo.html')
#         else:
#             return HttpResponse('login failed')
    
#     return render(request,'user_login.html')
    

    
    
