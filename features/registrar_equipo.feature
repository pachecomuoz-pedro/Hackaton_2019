Característica: Registrar Equipo
	Como participante
	Quiero registrar a mi equipo
	Para participar en el evento

	Escenario: Datos de registros correctos
		Dado que ingreso todos los datos del registro
		Cuando selecciono la opción Registrar equipo
		Entonces el equipo es registrado correctamente en el sistema y se notifica al usuario en ese momento.

	Escenario: Datos de registros incompletos
		Dado que faltan datos importantes en el registro
		Cuando selecciono la opción Registrar equipo
		Entonces se notifica al usuario que existen campos que aun no tienen datos.

	Escenario: Insertar tipos de datos no correspondientes
		Dado que inserto tipo de datos no correspondientes
		Cuando se esta llenado un campo del registro
		Entonces el sistema indica que no son  el tipo de dato correspondiente en rojo

	Escenario: Limite de caracteres
		Dado que el participante escribió en un apartado mas caracteres de lo permitido
		Cuando se esta enviando la duda
		Entonces  el sistema indica en rojo que el limite de caracteres