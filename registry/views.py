# Create your views here.
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from registry.models import Account

@csrf_exempt
def users(request):
    accountFilter = Account.objects.filter(pk = request.POST['username'])

    if accountFilter.count() > 0 :
        return HttpResponse(status = 404)
    else:
        try:
            accountTmp = Account(username = request.POST['username'], password = request.POST['password'], email = request.POST['email'])
            accountTmp.save()
        except:
            return HttpResponse(status = 404)
        else:
            return HttpResponse(status = 200)

