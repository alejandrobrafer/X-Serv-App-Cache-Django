from django.shortcuts import render
# Módulo de Python para realizar consultas a otros servicio web.
import urllib.request
from django.http import HttpResponse
from cache.models import Pages
import ssl

# Create your views here.

def url(request, url):
	try:
		page = Pages.objects.get(name=url)
		content = page.page
		response = ("Pagina caché")
	
	except Pages.DoesNotExist:
		response = ("Pagina nueva")
		# Implementado para evitar la excepcion [SSL: CERTIFICATE_VERIFY_FAILED]
		context = ssl._create_unverified_context()
		f = urllib.request.urlopen('http://' + url, context=context)
		content = f.read().decode('utf-8')
		new = Pages(name= url, page = content)
		new.save()
	
	return HttpResponse(response + content)
