# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from registry.models import Account
from django.shortcuts import get_object_or_404
import json
import uuid

@csrf_exempt
def users(request):
    #Create new account
    accountFilter = Account.objects.filter(username = request.POST['username'])

    if accountFilter.count() > 0 :
        response_data = {}
        response_data['status'] = "error"
        response_data['message'] = "The username have been registered."
        return HttpResponse(json.dumps(response_data), status = 200)
    else:
        try:
            uuidTmp = uuid.uuid1()
            accountTmp = Account(_id = str(uuidTmp), username = request.POST['username'], password = request.POST['password'], email = request.POST['email'])
            accountTmp.save()
        except:
            response_data = {}
            response_data['status'] = "error"
            response_data['message'] = "Something error!"
            return HttpResponse(json.dumps(response_data), status = 400)
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
