Característica: Descarga de datos participante
	Como organizador
	Quiero descargar todos los datos de los participantes
	Para llevar un control para las auditorias

	Escenario: Descarga de datos exitosa
		Dado que ingreso a los datos de un participante
		Cuando selecciono la opción descargar datos
		Entonces se comienza a descargar un archivo con todos los datos del participante

	Escenario: Descarga de datos erroneos
		Dado que los datos de los participantes no sean los solicitados
		Cuando selecciono la opción descargar datos
		Entonces vuelve a recargar pagina para una nueva descarga