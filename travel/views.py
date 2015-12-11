from django.shortcuts import render

# Create your views here.
def travel(request):

    print(request)
    context = {
        "title": "This is Travel Title"
    }
    render (request, "travel.html", context)