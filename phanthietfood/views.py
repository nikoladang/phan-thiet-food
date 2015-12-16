from django.shortcuts import render
from registration.backends.simple.views import RegistrationView

def index(request):

    context = {

    }

    return render(request, "index.html", context)

def food(request):

    context = {

    }

    return render(request, "food.html", context)

def fun(request):

    context = {

    }

    return render(request, "fun.html", context)

class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/'
