from django.shortcuts import render, redirect

# Create your views here.
def homepage(request):
    return redirect('login')

def login(request):
    return render(request, "login.html")