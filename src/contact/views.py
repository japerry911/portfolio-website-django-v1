from datetime import datetime

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render


def index(request):
    # if request.method == "POST":
    #     print("POST")
    #     return render(request, "contact.html")
    # else:
    #     return render(request, "contact.html")

    if request.method == "POST":
        try:
            name = request.POST["name"]
            email_address = request.POST["email_address"]
            message = request.POST["message"]

            email_message = f"""
            Name: {name}\n
            Email Address: {email_address}\n
            Message:\n{message}\n\n
            *Date Time Sent (UTC): {datetime.utcnow()}
            """

            _email(message=email_message)

            return HttpResponseRedirect("success")
        except KeyError:
            raise NotImplementedError

    return render(request, "contact.html")


def success(request):
    return render(request, "success.html")


def _email(message):
    subject = f"Portfolio Contact Submission (UTC): {datetime.utcnow()}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_HOST_USER]

    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
    )
