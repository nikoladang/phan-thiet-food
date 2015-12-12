import sys
import traceback

from django.shortcuts import render
from .forms import ContactForm

# from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives

# Create your views here.

def contact(request):
    title = "Welcome"
    # if request.user.is_authenticated():
    #     title = "%s -  Phan Thiet Food" % (request.user)
    if request.method == "POST":
        print(request.POST)
    form = ContactForm(request.POST or None)
    context = {
        "title": title,
        "form": form
    }

    if form.is_valid():
        print("FORM VALID")
        instance = form.save()

        # email sending
        try:
            mail_subject="[PhanThietFood] Contact | %s - %s" % (instance.full_name, instance.title)
            mail_body="Full name: " + instance.full_name + "<br>" + \
                        "Email: " + instance.email +  "<br>"  + \
                        "Phone: " + instance.phone +  "<br>"  + \
                        "Title: " + instance.title +  "<br>"  + \
                        "Message: " + instance.message
            mail_from_email="%s <ptf@phanthietfood.com>" % (instance.full_name)
            mail_to=["ptf@phanthietfood.com"]
            mail_headers={"Reply-To": "ptf@phanthietfood.com"}
            mail = EmailMultiAlternatives(
                subject=mail_subject,
                body=mail_body,
                from_email=mail_from_email,
                # from_email="Yamil Asusta <ptf@phanthietfood.com>",
                to=mail_to,
                headers=mail_headers
            )
            mail.attach_alternative(mail_body, "text/html")
            mail.send()
        except:
            print("Unexpected error:", sys.exc_info()[0])
            traceback.print_exc()
    else:
        print("FORM INVALID")

    return render(request, "contact2.html", context)