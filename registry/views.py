# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from registry.models import Account
from django.shortcuts import get_object_or_404, render
import json
import uuid

@csrf_exempt
def users(request) :
    # Create new account
    if request.method == 'POST' :
        accountFilter = Account.objects.filter(username = request.POST['username'])

        if accountFilter.count() > 0 : # if username have been registered before
            #response_data = {}
            #response_data['status'] = "error"
            #response_data['message'] = "The username have been registered."
            #return HttpResponse(json.dumps(response_data), status = 200)
            return render(request, 'sign/signup.html', {"status": "error", "message": "The username have been registered."}, status = 200)
        else :
            try :
                uuidTmp = uuid.uuid1()
                accountTmp = Account(_id = str(uuidTmp), username = request.POST['username'], password = request.POST['password'], email = request.POST['email'])
                accountTmp.save()
            except : # Some other error
                #response_data = {}
                #response_data['status'] = "error"
                #response_data['message'] = "Something error!"
                #return HttpResponse(json.dumps(response_data), status = 400)
                return render(request, 'sign/signup.html', {"status": "error", "message": "Something error!"}, status = 400)
            else :
                return HttpResponse(status = 200)
    else :
        return HttpResponse(status = 400)

@csrf_exempt
def detail(request, user_name) :
    # Show the detail of account
    if request.method == 'GET' :
        accountTmp = get_object_or_404(Account, username = user_name)
        return render(request, 'users/users.html', {"username": accountTmp.username, "email": accountTmp.email}, status = 200)
    else :
        return HttpResponse(status = 400)

@csrf_exempt
def signin(request) :
    # Login account
    if request.method == 'POST':
        try :
            accountTmp = Account.objects.get(username = request.POST['username'])
            if accountTmp.password == request.POST['password'] :
                request.session['account_id'] = accountTmp._id
                response_data = {}
                response_data['_id'] = accountTmp._id
                response_data['username'] = accountTmp.username
                response_data['email'] = accountTmp.email
                return HttpResponse(json.dumps(response_data), content_type = "application/json", status = 200)
            else : # Password error
                response_data = {}
                response_data['status'] = "error"
                response_data['message'] = "password error!"
                return HttpResponse(json.dumps(response_data), status = 400)
        except : # No that username
            response_data = {}
            response_data['status'] = "error"
            response_data['message'] = "There is no this user."
            return HttpResponse(json.dumps(response_data), status = 404)
    else :
        return HttpResponse(status = 400)

@csrf_exempt
def logout(request) :
    # Logout account
    if request.method == 'GET' :
        try :
            del request.session['account_id']
        except :
            response_data = {}
            response_data['status'] = "error"
            response_data['message'] = "No such session."
            return HttpResponse(json.dumps(response_data), status = 400)
        else :
            return HttpResponse(status = 200)
    else :
        return HttpResponse(status = 400)

@csrf_exempt
def myDetail(request):
    # Show detail about the login user
    if request.method == 'GET' :
        try :
            accountTmp = Account.objects.get(_id = request.session['account_id'])
            response_data = {}
            response_data['_id'] = accountTmp._id
            response_data['username'] = accountTmp.username
            response_data['email'] = accountTmp.email
        except :
            response_data = {}
            response_data['status'] = "error"
            response_data['message'] = "No such session."
            return HttpResponse(json.dumps(response_data), status = 400)
        else :
            return HttpResponse(json.dumps(response_data), status = 200)
    else :
        return HttpResponse(status = 400)
