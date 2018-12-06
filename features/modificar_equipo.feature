Característica: Modificar equipo
	Como lider del equipo
	Yo puedo actualizar datos del equipo
	Para cambiar datos (nuevos integrantes, eliminar integrantes)

	Escenario: Modificar Datos Equipo
		Dado que Modifico los datos del equipo correctamente
		Cuando selecciono la opción actualizar datos
		Entonces se me notifica que los datos han sido actualizados correctamente

	Escenario: Modificar Integrantes de Equipo
		Dado que Modifico integrantes del equipo
		Cuando selecciono la opción actualizar datos
		Entonces se me notifica que los datos han sido actualizados correctamente

	Escenario: Modificar datos del equipo dejando en blanco
		Dado que el líder de equipo dejo datos en blanco 
		Cuando se están actualizando los datos del equipo
		Entonces se marcaran los datos por llenar y deshabilitara la opción de actualizar hasta ser llenados

	Escenario: Insertar tipos de datos no correspondientes cuando se modifican los datos del equipo
		Dado que que inserto tipos de datos (numéricos o strings) no correspondientes
		Cuando se están modificando los datos del equipo
		Entonces el sistema indicará que no son  el tipo de dato correspondiente en rojo

	Escenario: limite de caracteres al modificar el equipo
		Dado que el líder del equipo escribió en un apartado mas caracteres de lo permitido
		Cuando se están actualizando los datos del equipo
		Entonces  el sistema indica en rojo que el limite de caracteres