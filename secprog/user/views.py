from django.shortcuts import render
from django.http import HttpResponse
from .models import User, PurchaseHistory

# Create your views here.
def profile(request, user_id):
    return HttpResponse("<h2>I am user " + str(user_id) + " yeah!</h2>")