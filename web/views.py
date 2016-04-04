from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from web.models import *
import datetime
import requests

	
def play(request):
	template = loader.get_template('play.html')
	return HttpResponse(template.render(request))
#TEST----------------------------------
def hora(request):
	ahora = datetime.datetime.now()
	html = "<html><body> Ahora es %s.</body></html>" % ahora
	return HttpResponse(html)
	
#-----------------------------------------
#Send_points Envia otra vez los datos recibidos del jugador junto a su puntuacion obtenida
def send_points(request):
	#dataPoints = {'token': 'tokenTest', 'validation': 'validationTest', 'invitation': 'invTest', 'percent': '5'}
	
	payload =  {'token': 'tokenTest', 'validation': 'validationTest', 'invitation': 'invTest', 'percent': '5'}
	
	r = requests.get('http://127.0.0.1:8000/web/ReceivePointsTest', params=payload)
	
	response = request.POST.get('html','')
	
	return HttpResponse(response)
	
def ReceivePointsTest(request):
	
	tokenId=request.GET.get('token','')
	validationId=request.GET.get('validation','')
	invitationId=request.GET.get('invitation','')
	percentId=request.GET.get('percent','')
	
	
	if (tokenId !='' and invitationId != '' and validationId != '' and percentId != ''):
		data = PointsT(token=tokenId, validation=validationId, invitation=invitationId, percent=percentId )
		data.save()
		
		html = "<html><body> RECIBIMOS ESTE POST <br> es: <br> asd.</body></html>"
		payload = {'html': '<html><body> RECIBIMOS ESTE POST <br> es: <br> asd.</body></html'}
		r = requests.post('http://127.0.0.1:8000/web/sendPost/', params=payload)

	
	
	return HttpResponse()
	
	
	
	
	
	