from django.shortcuts import render,redirect
from .models import materia

# Create your views here.

def index_view(request):
    materias=materia.objects.all()
    return render(request,'manageMat.html',{"mymaterias":materias})

def regMat(request):
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    creditos=request.POST['numcreditos']

    guardarmateria=materia.objects.create(codigo=codigo,nombre=nombre,creditos=creditos)
    return redirect('/')

def selectMat(codigo):
    materia.materia.objects.get(codigo=codigo)
    return render(request,"editMat.html",{"mymaterias":materia})

def editMat():
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    creditos=request.POST['numcreditos']
    materia.materia.objects.get(codigo=codigo)
    materia.nombre=nombre
    materia.creditos.creditos
    materia.save()
    return redirect('/')

def deleteMat(request,codigo):
    materia=materia.objects.get(codigo=codigo)
    materia.delete()

    return redirect("/")