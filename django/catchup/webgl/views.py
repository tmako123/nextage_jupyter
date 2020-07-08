from django.shortcuts import render
from django.http.response import JsonResponse

import zmq
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.bind("tcp://*:5555")

# Create your views here.

from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Hi Django~!!")

def index(request):
    return render(request, 'ply.html')
    
def slam(request):
	return render(request, 'slam.html')
    
def postPose(request):
    socket.send_string("ack")

    message = socket.recv_string()
    data = [float(x.strip()) for x in message.split(',') if not x.strip() == '']
    dict = {'frame':data[0], 'x':data[1], 'y':data[2], 'z':data[3], 'ax':data[4], 'ay':data[5], 'az':data[6], 'angle':data[7]}
    
    return JsonResponse(dict)
