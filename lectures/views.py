from django.shortcuts import render
from .models import Lectures

# Just using function based views for now because they're easy
def lectures_home(request):
    queryset = Lectures.objects.all()
    context = {
        "object_list": queryset,
    }
    return render(request, "lectures.html", context)