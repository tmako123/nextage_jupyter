from django.shortcuts import render_to_response

# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse

import json

def index(request):
    return render(request, 'button.html')

def multi_button(request):
    return render(request, 'multi_button.html')


def more(request):
    return render(request, 'more.html')

def ajax(request):
    return render(request, 'ajax_sample.html')

def ajax_get_json(request): 
    data = {'id': 1, 'name': 'hoge'}
    json_str = json.dumps(data, ensure_ascii=False, indent=2)
    return HttpResponse(json_str, content_type="application/json")