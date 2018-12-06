from django.shortcuts import render, redirect
from equipos.models import Equipo
from .forms import FormEquipo
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(redirect_field_name='login')
def lista_equipos(context):
	equipos = Equipo.objects.all()
	return render(context, 'lista_equipos.html', {'equipos':equipos})

def registro_equipo(context):
	if (context.method == 'POST'):
		form = FormEquipo(context.POST, context.FILES)
		if form.is_valid():
			equipo = form.save()
			equipo.save()
			return redirect('lista_equipos')
	else:
		form = FormEquipo()
	return render(context, 'registro_equipo.html',{'registro_equipo':form,'accion':'Nuevo'})

def editar_equipo(request, id):
	equipo = Equipo.objects.get(pk=id)
	if request.method == "POST":
		form = FormEquipo(request.POST, instance=equipo)
		if form.is_valid():
			equipo = form.save()
			equipo.save()
			return redirect('lista_equipos')
	else:
		form = FormEquipo(instance=equipo)
	return render(request, 'registro_equipo.html', {'registro_equipo': form,'accion':'Editar'})

def eliminar_equipo(request, id):
	try:
		equipo = Equipo.objects.get(pk=id)
		equipo.delete()
		return redirect('lista_equipos')
	except Equipo.DoesNotExist:
		equipo = Equipo.objects.all()
		return render(context, 'lista_equipos.html', {'equipos':equipos, 'error':'No se encuentra el equipo'})
