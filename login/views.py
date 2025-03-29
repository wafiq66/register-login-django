from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def get_login_applicant(request):
    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        #this method easily check if user exist or not
        user = authenticate(request,username=email,password=password)
        
        
        #will check whether there is user or not, and also determine the user type
        if user is not None:
            if user.user_type == "applicant":
                login(request, user)  # Logs the user in
                return redirect(reverse("landingpage:landing_page"))
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, "login_applicant.html")

def get_login_employer(request):
    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        #this method easily check if user exist or not
        user = authenticate(request,username=email,password=password)
        
        
        #will check whether there is user or not, and also determine the user type
        if user is not None:
            if user.user_type == "employer":
                login(request, user)  # Logs the user in
                return redirect(reverse("landingpage:landing_page"))
            else:
                messages.error(request, "Invalid email or password.")
        else:
            messages.error(request, "Invalid email or password.")

    return render(request, "login_employer.html")