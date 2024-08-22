from django.contrib.auth import login, authenticate
from django.http import HttpResponseRedirect

# create your views here.
def login_view(request, username, password):
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/django-admin/')
    else:
        return HttpResponseRedirect('/django-admin/login/')