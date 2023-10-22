from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import *

def index(request):
	danila  = User(name='danila', second_name='agapitov', password='12345678')
	ivan    = User(name='ivan', second_name='ladygin', password='kristinochka_moya_koroleva')
	mikhail = User(name='mikhail', second_name='shimenkov', password='cpp for life')
	timur   = User(name='timur', second_name='davletshin', password='where is arduino?...')

	danila.save()
	ivan.save()
	mikhail.save()
	timur.save()

	result = ''
	user_list = User.objects.all()
	for user in user_list:
		result += f'{user.name} {user.second_name} {user.password}<br>'

	return HttpResponse(result)