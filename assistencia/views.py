from django.shortcuts import render
from django.http import JsonResponse
from .models import Aparelho

def lista_aparelhos(request):
    marca = request.GET.get('marca')
    modelo = request.GET.get('modelo')
    
    if marca or modelo:
        aparelhos = Aparelho.objects.all()
        if marca:
            aparelhos = aparelhos.filter(marca=marca)
        if modelo:
            aparelhos = aparelhos.filter(modelo=modelo)
    else:
        aparelhos = Aparelho.objects.none()  # Não exibe nada se nenhum filtro for selecionado

    marcas = Aparelho.objects.values_list('marca', flat=True).distinct()
    
    return render(request, 'assistencia/lista_aparelhos.html', {'aparelhos': aparelhos, 'marcas': marcas})

def obter_modelos(request):
    marca = request.GET.get('marca')
    if marca:
        modelos = Aparelho.objects.filter(marca=marca).values_list('modelo', flat=True).distinct()
        return JsonResponse({"modelos": list(modelos)})
    return JsonResponse({"modelos": []})
