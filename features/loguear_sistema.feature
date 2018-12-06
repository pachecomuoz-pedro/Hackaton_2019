Característica: Logear al sistema
	Como usuario
	Quiero logearme al sistema
	Para entrar como participante u organizador

	Escenario: Iniciar Sesión excepción
		Dado que ingreso credenciales no validas "pedrop" y "pedrop456"
		Cuando selecciono la opción iniciar sesión
		Entonces se me notifica en pantalla "Usuario no válido"

	Escenario: Iniciar Sesión exito
		Dado que ingreso credenciales validas "pedrop" y "pedrop123"
		Cuando selecciono la opción iniciar sesión
		Entonces se mostrara la pagina principal del evento "Participantes"
