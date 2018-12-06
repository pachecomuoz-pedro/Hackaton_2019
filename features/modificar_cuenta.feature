Característica: Modificar Cuenta
	Como participante
	Quiero cambiar datos personales del registro
	Para actualizar algun dato que este (mal, nuevo)

	Escenario: Actualizar Datos Correctamente
		Dado que edito información de mi perfil
		Cuando selecciono la opción actualizar datos
		Entonces Los datos son actualizados de forma correcta.

	Escenario: Actualizar datos dejando en blanco
		Dado que el participante dejo datos en blanco 
		Cuando selecciono la opción de  actualizar sus datos
		Entonces se marcaran los datos por llenar y des habilitara la opción de actualizar hasta ser llenados

	Escenario: Actualizo datos con tipo de datos no correspondientes
		Dado que inserto tipos de datos (numericos o strings)no correspondientes
		Cuando se están modificando los datos
		Entonces el sistema indica que no son  el tipo de dato correspondiente en rojo