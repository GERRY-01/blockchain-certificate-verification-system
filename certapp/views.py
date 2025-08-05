from django.shortcuts import render,redirect
from .utils import generate_hash
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login as auth_login
from certapp.models import Institution

# Create your views here.
def index(request):
    return render(request,'index.html')

def verification(request):
    return render(request,'verification.html')

def register(request):
    if request.method == 'POST':
        institution_name = request.POST.get('institution_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        
        if Institution.objects.filter(institution_name=institution_name).exists():
            messages.error(request, 'Institution name already exists')
            return redirect('register')

        if password == confirm_password:
            #save the details to the user and institution table
            user = User.objects.create_user(username=email, email=email, password=password)
            user.save()

            institution = Institution(user=user, institution_name=institution_name)
            #generate a hash for the institution
            institution_hash = generate_hash(institution_name)
            institution.institution_hash = institution_hash
            institution.save()
            messages.success(request, 'Registration successful')
            return redirect('login')
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid email or password')
    return render(request,'login.html')