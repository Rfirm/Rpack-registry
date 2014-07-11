# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from registry.models import Account
from django.shortcuts import get_object_or_404
import json

@csrf_exempt
def users(request):
    accountFilter = Account.objects.filter(pk = request.POST['username'])

    if accountFilter.count() > 0 :
        return HttpResponse("There is same username in database",status = 404)
    else:
        try:
            accountTmp = Account(username = request.POST['username'], password = request.POST['password'], email = request.POST['email'])
            accountTmp.save()
        except:
            return HttpResponse("Something error!", status = 404)
        else:
            return HttpResponse(status = 200)

@csrf_exempt
def detail(request, user_name):
    if request.method == 'GET' :
        accountTmp = get_object_or_404(Account, pk = user_name)
        response_data = {}
        response_data['username'] = accountTmp.username
        response_data['email'] = accountTmp.email
        return HttpResponse(json.dumps(response_data), status = 200)
    else :
        return HttpResponse(status = 404)
