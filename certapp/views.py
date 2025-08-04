from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def verification(request):
    return render(request,'verification.html')