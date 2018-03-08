from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
def index(request):
    return render(request,'first/index.html')

def register(request):
    userReg.objects.filter(username=request.POST['username'])
    result = userReg.objects.user_validation(request.POST)

    if result[0]:
        request.session['user_id']= result[1].id
        peep = request.POST['username']
        request.session['peep'] = peep
        return redirect('/second/')
    else:
        for err in result[1]:
            messages.error(request, err)
        return redirect('/')
def login(request):
    result = userReg.objects.login_validation(request.POST)
    if result[0]:
        request.session['user_id']= result[1][0].id
        peep = request.POST['username']
        request.session['peep'] = peep
        return redirect('/second/')
    else:
        for i in result[1]:
            messages.error(request, i)
        return redirect('/')