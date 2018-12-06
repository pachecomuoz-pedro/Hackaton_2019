Característica: Baja cuenta
	Como participante
	Quiero eliminar cuenta
	Para confirmar que ya no participare en el evento

	Escenario: Baja de cuenta exitosa
		Dado que Ingreso a la sección del perfil
		Cuando selecciono la opción, dar de baja.
		Entonces se cerrara la sesión y se notificara al usuario que su cuenta fue dada de baja de forma exitosa.

	Escenario: No se eliminó la cuenta
		Dado que no se eliminó el cuenta
		Cuando se presionó el botón de eliminar
		Entonces se notificará que no se eliminó y podrá intentar nuevamente