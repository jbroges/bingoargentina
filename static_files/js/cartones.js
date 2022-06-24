

/**** SETTINGS AJAX ****/
    $(document).ajaxStart(function() {
        $(':button[type="submit"]').html('<img src="http://dockrealty.biz/images/preloader2.gif" width="20px">');
        $(':button[type="submit"]').attr('disabled','disabled');   
        $(':button[type="button"]').attr('disabled','disabled');   
    });
    $(document).ajaxStop(function() {
        $(':button[type="submit"]').html('Guardar');
        $(':button[type="submit"]').removeAttr('disabled');
        $(':button[type="button"]').removeAttr('disabled');
    });

/**** COMTROL DE ERRORES ****/
function scrollToID(element,idError,msj){
  $(idError).show();
  $(idError + 'BR').show();
  $(idError + ' span').html(msj);
  $('html, body').animate({
        scrollTop: $(idError).offset().top - 100
    }, 'slow');
  $(element).css('border','2px solid red');
}

//ESCONDE EL SALTO DE LINEA
function ErrorHide(idError){
  $(idError).hide();
  $(idError + 'BR').hide();

}

/**** ENVIAR AJAX DE CREAR Asignación ****/
$( "#addAsig" ).submit(function( event ) {


if($('#id_partida').val()==''){
    scrollToID('#id_partida','#ErrorFecha','Debe Seleccionar la Partida');
    return false;
  }else{
    ErrorHide('#ErrorFecha');
    $('#id_partida').css('border','1px solid #C7C7CC');
  }

if($('#id_correlat_ini').val()==''){
    scrollToID('#id_correlat_ini','#ErrorNumInc','Debe indicar el correlatvo inicial');
    return false;
  }else{
    ErrorHide('#ErrorNumInc');
    $('#id_correlat_ini').css('border','1px solid #C7C7CC');
  }

if($('#id_correlat_fin').val()==''){
    scrollToID('#id_correlat_fin','#ErrorNumFin','Debe indicar el correlatvo final');
    return false;
  }else{
    ErrorHide('#ErrorNumFin');
    $('#id_correlat_fin').css('border','1px solid #C7C7CC');
  }


   $.ajax({
           type: "POST",
           url: '/carton/asignacion/crear/',
           data: $( "#addAsig" ).serialize(), // serializes the form's elements.           
           success: function(data)
           {

             if(data=='ok'){
                  setTimeout("location.href='/carton/asignacion/'", 300);

              }else{
                scrollToID('#id_sala','#ErrorSala','La sala ya tiene Asignación para la Partida');
              }
           }
         });
  event.preventDefault();
});

/**** ENVIAR AJAX DE EDITAR Asignación ****/
$( "#editAsig" ).submit(function( event ) {


if($('#id_partida').val()==''){
    scrollToID('#id_partida','#ErrorFecha','Debe Seleccionar la Partida');
    return false;
  }else{
    ErrorHide('#ErrorFecha');
    $('#id_partida').css('border','1px solid #C7C7CC');
  }

 
if($('#id_correlat_ini').val()==''){
    scrollToID('#id_correlat_ini','#ErrorNumInc','Debe indicar el correlatvo inicial');
    return false;
  }else{
    ErrorHide('#ErrorNumInc');
    $('#id_correlat_ini').css('border','1px solid #C7C7CC');
  }

if($('#id_correlat_fin').val()==''){
    scrollToID('#id_correlat_fin','#ErrorNumFin','Debe indicar el correlatvo final');
    return false;
  }else{
    ErrorHide('#ErrorNumFin');
    $('#id_correlat_fin').css('border','1px solid #C7C7CC');
  }
document.getElementById("id_partida").disabled = false;
  
   $.ajax({
           type: "POST",
           url: '/carton/asignacion/editar/' + $('#id_id').val() + '/',
           data: $( "#editAsig" ).serialize(), // serializes the form's elements.           
           success: function(data)
           {

             if(data=='ok'){
                  setTimeout("location.href='/carton/asignacion/'", 300);

              }
           }
         });
  event.preventDefault();
});

//BORRAR ITEM //
function BorrarAsig(id,csrf_token){

 if (confirm('¿Estas seguro de eliminar esta Asignación?')) {
           $.ajax({
                   type: "POST",
                   url: 'eliminar/' + id + '/',
                   data: { 'pk' : id,'csrfmiddlewaretoken': csrf_token },

                   success: function(data)
                   {
                      if(data=='ok'){
                          alert('Eliminado exitosamente');
                          $("#" + id + "_fila").fadeOut("slow");
                      }
                   }
                 });
    }

    return false;

}


$('#btnBusCliente').click(function(){
if($('#id_cliente').val()==''){
    document.getElementById("imprimir").disabled = true;
    scrollToID('#id_cliente','#ErrorCliente','Debe indicar el numero de cédula del cliente');
    return false;
  }else{
    ErrorHide('#ErrorCliente');
    $('#id_cliente').css('border','1px solid #C7C7CC');
  }  

  $.get('/cliente/verificar/',{cedula:$('#id_cliente').val()})
  .done(function(data){
    if(data=='NoExiste'){
      document.getElementById("imprimir").disabled = true;
      scrollToID('#id_cliente','#ErrorCliente','Cliente No existe <a href="/cliente/crear/">Crear</>');
      document.getElementById("imprimir").disabled = false;
    }else{

      document.getElementById("id_nombre").value= data.nombre;
      document.getElementById("id_telefono").value= data.telefono;
      document.getElementById("imprimir").disabled = false;
      ErrorHide('#ErrorCliente');
    }
  });
  return false;
});


/**** ENVIAR AJAX DE ANULAR ****/
$( "#anular" ).submit(function( event ) {


if($('#id_partida').val()==''){
    scrollToID('#id_partida','#ErrorFecha','Debe Seleccionar la Partida');
    return false;
  }else{
    ErrorHide('#ErrorFecha');
    $('#id_partida').css('border','1px solid #C7C7CC');
  }

if($('#id_numcarton').val()==''){
    scrollToID('#id_numcarton','#ErrorNumInc','Debe indicar el Numero de Carton');
    return false;
  }else{
    ErrorHide('#ErrorNumInc');
    $('#id_numcarton').css('border','1px solid #C7C7CC');
  }



   $.ajax({
           type: "POST",
           url: '/carton/asignacion/anular/',
           data: $( "#anular" ).serialize(), // serializes the form's elements.           
           success: function(data)
           {

             if(data=='ok'){
              alert('Se Anulo Satisfactoriaente');
                  setTimeout("location.href='/'", 300);

              }else{
                scrollToID('#id_sala','#ErrorSala','La sala ya tiene Asignación para la Partida');
              }
           }
         });
  event.preventDefault();
});