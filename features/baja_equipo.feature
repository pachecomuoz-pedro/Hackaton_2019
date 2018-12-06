Característica: Baja equipo
	Como lider del equipo
	Quiero eliminar mi equipo
	Para confirmar que no se participara en el evento

	Escenario: No se elimino el equipo
		Dado que no se eliminó el equipo
		Cuando presionó el botón de eliminar equipo 
		Entonces se notificará que no se eliminó y podrá intentar nuevamente

	Escenario: Baja de equipo exitosa
		Dado que Ingreso al apartado de un equipo
		Cuando selecciono la opción dar de baja equipo
		Entonces el equipo es eliminado y se me notifica en pantalla que el equipo ya no existe y ya no pertenezco a el
		