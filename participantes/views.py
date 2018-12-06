from django.shortcuts import render, redirect
from participantes.models import Participante, Estado, Municipio
from .forms import FormParticipante
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import simplejson

# Create your views here.
@login_required(redirect_field_name='login')
def entrar(context):
    return render(context, 'participantes.html')

def lista_participantes(context):
    participantes = Participante.objects.all()
    return render(context, 'lista_participantes.html', {'participantes':participantes})

def mostrar_mapa(context):
    return render(context, 'mapa.html')

def carga_municipio(request):
    estado = Estado.objects.get(id=request.GET.get('id',''))

    municipios = Municipio.objects.filter(estado=estado)
    municipiosJson = []
    for municipio in municipios:
        municipiosJson.append(
            {
                'id': municipio.id,
                'municipio': municipio.municipio
            }
        )

    data = simplejson.dumps(municipiosJson)
    return HttpResponse(data, content_type="application/json")

def registro_participante(context):
    if (context.method == 'POST'):
       form = FormParticipante(context.POST, context.FILES)
       if form.is_valid():
           participante = form.save()
           participante.save()
           return redirect('lista_participantes')
    else:
        form = FormParticipante()
    return render(context, 'registro_participante.html',{'registro_participante':form,'accion':'Nuevo'})

def editar_participante(request, id):
    participante = Participante.objects.get(pk=id)
    if request.method == "POST":
        form = FormParticipante(request.POST, instance=participante)
        if form.is_valid():
            participante = form.save()
            participante.save()
            return redirect('lista_participantes')
    else:
        form = FormParticipante(instance=participante)
    return render(request, 'registro_participante.html', {'registro_participante': form,'accion':'Editar'})

def eliminar_participante(request, id):
    participante = Participante.objects.get(pk=id)
    participante.delete()
    return redirect('lista_participantes')