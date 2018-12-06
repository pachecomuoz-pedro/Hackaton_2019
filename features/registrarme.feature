Característica: Registrarme
	Como participantes
	Quiero registrarme
	Para poder participar en el evento

	Escenario: Registro de Usuario Exitoso
		Dado que completo el formulario de registro correctamente
		Cuando selecciono la opción registrar
		Entonces se me notifica que eh sido registrado correctamente.

	Escenario: Datos en blanco
		Dado que el usuario/participante deje un dato en blanco
		Cuando se este llenado el formulario
		Entonces la pagina mostrara los datos obligatorios que deben de ser llenados y no se activara el boton de registro

	Escenario: Limite de caracteres
		Dado que el usuario/participante escribió en un apartado mas caracteres de lo permitido
		Cuando se insertan los datos en el registro
		Entonces el sistema indica en rojo que el limite de caracteres se ha sobrepasado

	Escenario: Insertar tipos de datos no correspondientes
		Dado que inserto tipo de datos (numericos o strings) no correspondientes
		Cuando se esta llenado un campo del registro
		Entonces el sistema indica que no son  el tipo de dato correspondiente en rojo