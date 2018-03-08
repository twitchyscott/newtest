from django.shortcuts import render, redirect
from models import *
from ..user_app.models import userReg
def index(request):
    userinfo=userReg.objects.get(id=request.session['user_id'])
    event_all=active.objects.exclude(join=userinfo)
    event_all_active=active.objects.filter(join=userinfo)
    return render(request,'second/index.html', {'all':event_all, 'all_join':event_all_active})
def logout(request):
    request.session.flush()
    return redirect('/')
def add(request):
    return render(request, 'second/new.html')
def event(request,id):
    active_idr=active.objects.get(id=id)
    active_info=active.objects.exclude(join=id)
    active_event=active.objects.filter(join=id)
    context={
        "a_id":active_idr,
        "a_info":active_info,
        "a_eventdf":active_event
    }
    return render(request, 'second/event.html',context)
def create(request):
    print 'duck'
    activitie=active.objects.create(
    title=request.POST['title'],
    start=request.POST['start_time'],
    fin=request.POST['fin_time'],
    description=request.POST['descrip'],
    activity=userReg.objects.get(id=request.session['user_id']))
    activitie.save()
    return redirect('/second/')
def adder(request,id):
    user=userReg.objects.get(id=request.session['user_id'])
    new=active.objects.get(id=id)
    new.join.add(user)
    new.save()
    return redirect('/second/')
def remove(request,id):
    user=userReg.objects.get(id=request.session['user_id'])
    new=active.objects.get(id=id)
    new.join.remove(user)
    return redirect('/second/')
def delete(request,id):
    delIdea= active.objects.get(id=id)
    delIdea.delete()
    return redirect('/second/')