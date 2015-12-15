from django.shortcuts import render

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