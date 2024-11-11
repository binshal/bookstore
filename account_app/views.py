from django.shortcuts import render
from django.http import HttpResponse
from my_app.models import book, Author
from django.contrib import messages
from django.shortcuts import redirect
from my_app.forms import AuthorForm,BookForm
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from . models import UserProfile,loginTable

# Create your views here.
def UserRegistration(request):
    login_table = loginTable()
    user_profile = UserProfile()

    if request.method == 'POST':
        user_profile.username = request.POST['username']
        user_profile.password = request.POST['password']
        user_profile.password2 = request.POST['password1']

        login_table.username = request.POST['username']
        login_table.password = request.POST['password']
        login_table.password2 = request.POST['password1']
        login_table.type = 'user'

        if request.POST['password'] == request.POST['password1']:
            user_profile.save()
            login_table.save()

            messages.info(request, 'Registration success')
            return redirect('login')

        else:
            messages.info(request, "Password doesn't match")
            return redirect('register')

    return render(request, 'accounts/accregister.html')

def loginPage(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = loginTable.objects.filter(username=username,password=password,type='user').exists()

        try:
            if user is not None:
                user_details = loginTable.objects.get(username=username,password=password)
                user_name = user_details.username
                type = user_details.type

                if type =='user':
                    request.session['username']=user_name
                    return redirect('userbooklist')
                elif type=='admin':
                    request.session['username'] = user_name
                    return redirect('booklist')

            else:
                messages.error(request,'invalid username or password')

        except:
            messages.error(request,'invalid role')

    return render(request,'accounts/acclogin.html')

def logout_view(request):
    logout(request)
    return redirect('login')



# def register(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         cpassword = request.POST.get('cpassword')
#
#         if password == cpassword:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request, 'This username already exists')
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request, 'This email already exists')
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
#                                                 email=email, password=password)
#                 user.save()
#                 return redirect('login')
#
#         else:
#             messages.info(request, 'This password does not match')
#             return redirect('register')
#
#     return render(request, 'accounts/register.html')
#
#
# def loginUser(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = auth.authenticate(username=username, password=password)
#
#         if user is not None:
#             auth.login(request, user)
#             return redirect('home')
#         else:
#             messages.info(request, 'Provide correct details')
#             return redirect('login')
#
#     return render(request, 'accounts/login.html')
#
#
# def logout(request):
#     auth.logout(request)
#     return redirect('login')
#
#
# def homepage(request):
#     return render(request, 'accounts/home.html')
