from django.shortcuts import render
from django.http import JsonResponse
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
from trade.models import User,Token,product
from datetime import datetime
# Create your views here.
@csrf_exempt
def submit_product(request):
    #TODO: valied data

    return render(request,'signup.html',{})
