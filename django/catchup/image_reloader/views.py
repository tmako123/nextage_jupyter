from django.shortcuts import render
from django.http.response import JsonResponse

# Create your views here.
import time


def index(request):
    return render(request, 'index.html')

def next_img(request):
    ut = time.time()
    int_ut = int(ut)
    img_num = int_ut % 10
    return JsonResponse({"res":img_num})