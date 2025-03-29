from django.shortcuts import render

# Create your views here.
def password_reset_form(request):
    return render(request, "password_reset_form.html")



#will be review later
def password_reset_done(request):
    return render(request, "password_reset_done.html")

def password_reset_confirm(request):
    return render(request, "password_reset_confirm.html")

def password_reset_complete(request):
    return render(request, "password_reset_complete.html")