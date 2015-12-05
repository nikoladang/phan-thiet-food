from django.contrib import admin

# Register your models here.
from .forms import ContactForm
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ["__str__", "timestamp", "updated"]
    form = ContactForm
    # class Meta:
    #     model = Contact

admin.site.register(Contact, ContactAdmin)
