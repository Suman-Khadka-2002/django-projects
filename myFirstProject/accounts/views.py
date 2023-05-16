from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):

    if request.method == 'POST':  # post data
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if (password1 == password2):
            if User.objects.filter(username = username).exists():
                print('Username already taken.')
            elif User.objects.filter(email = email).exists():
                print("Email already taken.")
            else:
                user = User.objects.create_user(username=username, password = password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                print('User created.') #prints in console after the user is created
                

        else:
            print("password not matching.")

        return redirect('/')  # redirects to homepage
    
    else:
        return render(request, 'register.html') # get data