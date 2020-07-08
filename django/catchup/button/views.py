# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

import json
import datetime

def index(request):
    return render(request, 'button.html')

def multi_button(request):
    return render(request, 'multi_button.html')


def more(request):
    return render(request, 'more.html')

def ajax(request):
    return render(request, 'ajax_sample.html')

def json_receive(request):
    print("received")
    jsondata = request.POST['value1']
    datas = json.loads(jsondata)
    print(jsondata)
    return JsonResponse({"res":"ok"})
        
count = 0
def json_send(request):
    dt_now = datetime.datetime.now()
    json_data = {"date":dt_now}
    return JsonResponse(json_data)