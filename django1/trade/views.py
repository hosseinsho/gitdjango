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

    if('name' in request.GET):
        #this_token = 123456
        #this_user = User.objects.filter(token__token = this_token).get()
        product.objects.create(product_name =  request.GET['name'], product_price = int(request.GET['price']))
    return render(request,'product.html',{})
