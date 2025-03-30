from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib import messages

# Create your views here.
UserAccount = get_user_model()

#Method to send email
def send_custom_email(user, request):
    uid = urlsafe_base64_encode(force_bytes(user.pk))  # Encode user ID
    token = default_token_generator.make_token(user)  # Generate secure token
    reset_url = request.build_absolute_uri(f"/forgot-password/confirm/{uid}/{token}/")

    subject = "🔑 Reset Your Password"
    
    # Render the email template
    html_message = render_to_string("password_reset_email.html", {
        "user": user,
        "reset_url": reset_url,
        "expiration_time": 15,  # Token expires in 15 minutes
    })

    # Send email with HTML formatting
    email = EmailMultiAlternatives(subject, "Click the link below to reset your password", settings.DEFAULT_FROM_EMAIL, [user.email])
    email.attach_alternative(html_message, "text/html")
    email.send()

#Use to receive user's email.
def password_reset_form(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        user = UserAccount.objects.filter(username=email).first()

        #The email will be checked first either exist or not
        if user is not None:
            send_custom_email(user, request)
            return redirect(password_reset_done)
        
        #If email doesnt exist it will be redirected back to the main page
        else:
            messages.error(request,"Email is not registered")
            return redirect(password_reset_form)

    return render(request, "password_reset_form.html")

#to tell the user that the reset link has been successfully sent 
def password_reset_done(request):
    return render(request, "password_reset_done.html")

#the user can update their password here
def password_reset_confirm(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = get_object_or_404(UserAccount, pk=uid)

        # Check if token is valid
        if default_token_generator.check_token(user, token):
            if request.method == 'POST':
                new_password = request.POST.get("password1")
                confirm_password = request.POST.get("password2")

                if new_password == confirm_password:
                    user.set_password(new_password)
                    user.save()
                    return redirect("password_reset_complete")
                else:
                    messages.error(request, "Passwords do not match.")

    except Exception:
        messages.error(request, "Invalid or expired link.")
        return redirect("password_reset_form")

    return render(request, "password_reset_confirm.html", {"uidb64": uidb64, "token": token})

#successfully update their password
def password_reset_complete(request):
    return render(request, "password_reset_complete.html")