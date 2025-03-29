from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

UserAccount = get_user_model()

# Create your views here.
def get_register_applicant(request):
    if request.method == "POST":

        #To check whether the email has been registered or not
        username = request.POST.get("email")
        if UserAccount.objects.filter(username=username).exists():
            messages.error(request, "Email is already taken.")
            return redirect(get_register_applicant)  # Change this to your actual register URL name

        #To check whether password is same or not with confirm password
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            messages.error(request,"Password doesn't match.")
            return redirect(get_register_applicant)

        registerAccount(request)
        return redirect(get_register_applicant)
            

    return render(request, "register_applicant.html")

def get_register_employer(request):

    if request.method == "POST":
        
        #To check whether the email has been registered or not
        username = request.POST.get("email")
        if UserAccount.objects.filter(username=username).exists():
            messages.error(request, "Email is already taken.")
            return redirect(get_register_employer)  # Change this to your actual register URL name

        #To check whether password is same or not with confirm password
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        if password1 != password2:
            messages.error(request,"Password doesn't match.")
            return redirect(get_register_employer)
        
        registerAccount(request)
        return redirect(get_register_employer)
        
    return render(request, "register_employer.html")

def registerAccount(request):
    username = request.POST.get("email")
    email = request.POST.get("email")
    password1 = request.POST.get("password1")
    user_type = request.POST.get("user_type")  # Either 'applicant' or 'employer'
    first_name = request.POST.get("fname")
    last_name = request.POST.get("lname")
    company_name = request.POST.get("company_name") if user_type == "employer" else None

    if username and email and password1 and user_type:

        user = UserAccount.objects.create(
            username=username,
            email=email,
            password=make_password(password1),  # Hash the password
            user_type=user_type,
            first_name=first_name,
            last_name=last_name,
            company_name=company_name,
        )
        messages.success(request, "Registration Successful!")