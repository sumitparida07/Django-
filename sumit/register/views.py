# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import login
# from django.contrib.auth import logout
# from django.contrib.auth import authenticate, login 
# from django.contrib import messages
# # Create your views here.
# def register(request):
#     if request.method == 'post':
#         first_name = request.post['first_name']
#         last_name = request.post['last_name']
#         username = request.post.get('username')
#         email = request.post['email']
#         password1 = request.post['password1']
#         password2 = request.post.get('password2')
#         # Check if password match
#         if password1 != password2:
#             return render(request, 'register.html', {'error': 'Passwords do not match.'})
        
#         # Check if username already exists
#         if User.objects.filter(username=username).exists():
#            return render(request, 'register.html', {'error': 'Username already taken.'}) 
        
#         # Check if email already exists
#         if User.objects.filter(email=email).exists():
#            return render(request, 'register.html', {'error': 'Email already registered.'}) 
        
#         # If everything is okay, create a new user 
#         user = user.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
#         user.save()

#         # Optionally log the user in immediately after registration
#         login(request, user)

#         # Redirect to the homepage or a success page
#         return redirect('index') # Change 'index' to the appropriate name of your homepage
    
#     return render(request, 'register.html')




from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Check if passwords match
        if password1 != password2:
            return render(request, 'register.html', {'error': 'Passwords do not match.'})

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already taken.'})

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already registered.'})

        # If everything is okay, create a new user
        user = User.objects.create_user(username=username, password=password1, email=email, 
                                        first_name=first_name, last_name=last_name)
        user.save()

        # Optionally log the user in immediately after registration
        login(request, user)

        # Redirect to the homepage or a success page
        return redirect('index')  # Change 'index' to the appropriate name of your homepage

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login the user
            login(request, user)
            return redirect('index')  # Redirect to homepage or desired page
        else:
            # If authentication fails
            return render(request, 'login.html', {'error': 'Invalid username or password.'})

    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to the login page or another page after logout