from django.http import response
from django.shortcuts import render

# Create your views here.


def home(request):
    vars = {
        'key': 'value'
    }

    return render(request, 'hello/home.html', vars)