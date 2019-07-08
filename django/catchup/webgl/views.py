from django.shortcuts import render_to_response

# Create your views here.
from django.shortcuts import render

from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Hi Django~!!")

def index(request):
    return render(request, 'ply.html')