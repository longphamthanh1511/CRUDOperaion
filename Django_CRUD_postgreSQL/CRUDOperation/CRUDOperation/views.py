from django.shortcuts import render
from CRUDOperation.models import ChimModel
from django.contrib import messages
from CRUDOperation.forms import chimforms

def showchim(request):
    showall=ChimModel.objects.all()
    return render(request, 'Index.html',{"data":showall})

def themchim(request):
    if request.method=="POST":
        if request.POST.get('chimcuaai') and request.POST.get('email') and request.POST.get('docong') and request.POST.get('dodai') and request.POST.get('sizechim'):
            chimthem=ChimModel()
            chimthem.chimcuaai=request.POST.get('chimcuaai')
            chimthem.email=request.POST.get('email')
            chimthem.docong=request.POST.get('docong')
            chimthem.dodai=request.POST.get('dodai')
            chimthem.sizechim=request.POST.get('sizechim')
            chimthem.save()
            messages.success(request, 'Chim của ' + chimthem.chimcuaai+ ' đã vào chuồng')
            return render(request, 'insert.html')
    else:
        return render(request, 'insert.html')
    
def suachim(request,id):
    chimsua=ChimModel.objects.get(id=id)
    return render(request, 'edit.html',{"ChimModel":chimsua})

def updatechim(request,id):
    Updatechim=ChimModel.objects.get(id=id)
    form=chimforms(request.POST,instance=Updatechim)
    if form.is_valid():
        form.save()
        messages.success(request, 'Chim của ' + Updatechim.chimcuaai+ ' đã duoc sua')
        return render(request, 'edit.html',{"ChimModel":Updatechim})

def xoachim(request,id):
    chimxoa=ChimModel.objects.get(id=id)
    chimxoa.delete()
    showall=ChimModel.objects.all()
    return render(request, 'Index.html',{"data":showall})
