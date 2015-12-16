from django.shortcuts import render

# Create your views here.
def travel(request):

    context = {
        "title": "This is Travel Title",
    }

    return render(request, "travel.html", context)
