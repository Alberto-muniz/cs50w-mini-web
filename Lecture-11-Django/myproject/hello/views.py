from django.shortcuts import render

# Create your views here.

from .models import Computer

def index(request):
    computers = Computer.objects.all()
    return render(request, "hello/index.html", {
        "computers": computers
    })