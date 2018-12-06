Característica: Recibir confirmacion
	Como participante 
	Quiero recibir confirmación
	Para comprobar que estoy registrado

	Escenario: Confirmación Participante
		Dado que hice mi registro en la pagina
		Cuando seleccione la opción de registrarme
		Entonces se confirmo que mi registro fue dado de alta de forma exitosa.

	Escenario: Ingresar correo invalido
		Dado que el participante ingreso un correo invalido
		Cuando envia el correo de confirmación
		Entonces  existirá la opción de volver a escribir el correo