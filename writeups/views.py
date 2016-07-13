from django.shortcuts import render, get_object_or_404
from .models import Writeups


def writeups_home(request):
    queryset = Writeups.objects.all()
    context = {
        "object_list": queryset,
    }
    return render(request, "writeups-main.html", context)


def writeups_detail(request, id):
    instance = get_object_or_404(Writeups, id=id)
    context = {
        "instance": instance,
    }
    return render(request, "writeup.html", context)