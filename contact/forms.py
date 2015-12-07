from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["full_name", 'email', 'phone', 'title', 'message']

    def clean_email(self):
        print(self.cleaned_data)
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        if not extension == "edu":
            raise forms.ValidationError("Please use a valid email!")
        return(email)
    #
    # def clean_phone(self):
    #     print(self.cleaned_data)
    #
    #     return("111")

    def clean_message(self):
        message = self.cleaned_data.get('message')
        print("zzzzzz"+message)
        if not message:
          return "NOT"
        else:
          return "OK"