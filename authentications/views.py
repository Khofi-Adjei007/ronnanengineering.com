from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


# Create your views here.
def home_view(request):
    return render(request, 'home_page.html')
