$('#id_estado').change(function(){
    $.ajax({
        data : {'id':$('#id_estado').val()},
		url : '/participantes/carga_mun',
		type : 'GET',
		success: function(data){
            $('#id_municipio').children().remove();
			for (i=0;i<data.length;i++)
            {
                $("#id_municipio").append('<option value='+data[i]['id']+'>'+data[i]['municipio']+'</option>');
            }
		},
		error : function(xhr,errmsg,err) {
	        console.log(xhr.responseText);
	    }
    });
});


function eliminarModalParticipante(url, participante) {
    document.getElementById('btnEliminarP').href=url;
    document.getElementById('btnModalP').click();
    document.getElementById('pParticipante').innerHTML="¿Estás seguro de eliminar al participante <strong>" + participante + "</strong>?";
}

function eliminarModalEquipo(url, equipo) {
    document.getElementById('btnEliminarE').href=url;
    document.getElementById('btnModalE').click();
    document.getElementById('pEquipo').innerHTML="¿Estás seguro de eliminar al equipo <strong>" + equipo + "</strong>?";
}