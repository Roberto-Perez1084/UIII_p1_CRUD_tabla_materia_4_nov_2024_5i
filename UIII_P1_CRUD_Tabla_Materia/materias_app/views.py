from django.shortcuts import render
from .models import materia

# Create your views here.

def index_view(request):
    lasmaterias=materia.objects.all()
    return render(request,'manageMat.html')