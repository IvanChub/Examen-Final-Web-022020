from django.http import HttpResponse
from django.shortcuts import render

from core.erp.models import Categoria


def vistaCategoria(request):
    data ={
        'nombre': 'Ivan',
        'categoria': Categoria.objects.all()
    }
    return render(request,'home.html', data)