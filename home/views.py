from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    if request.method == 'GET':
        return render (request, 'index.html')




# Create your views here.
