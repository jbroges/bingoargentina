
/**** SETTINGS AJAX ****/
    $(document).ajaxStart(function() {
        $(':button[type="submit"]').html('<img src="http://dockrealty.biz/images/preloader2.gif" width="20px">');
        $(':button[type="submit"]').attr('disabled','disabled');   
        $(':button[type="button"]').attr('disabled','disabled');   
    });
    $(document).ajaxStop(function() {
        $(':button[type="submit"]').html('Guardar');
        $('#buscarBtn').html('<i class="fa fa-search">');
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

/**** ENVIAR AJAX DE CREAR PARTIDA ****/
$( "#addPartida" ).submit(function( event ) {



if($('#id_fecha').val()==''){
    scrollToID('#id_fecha','#ErrorFecha','Debe indicar la Fecha');
    return false;
  }else{
    ErrorHide('#ErrorFecha');
    $('#id_fecha').css('border','1px solid #C7C7CC');
  }

if($('#id_organiza').val()==''){
    scrollToID('#id_organiza','#ErrorOrganiza','Debe indicar al Organizador');
    return false;
  }else{
    ErrorHide('#ErrorOrganiza');
    $('#id_organiza').css('border','1px solid #C7C7CC');
  }

 if($('#id_sorteo').val()==''){
    scrollToID('#id_sorteo','#ErrorSorteo','Debe indicar al Dia y Hora del Sorteo');
    return false;
  }else{
    ErrorHide('#ErrorSorteo');
    $('#id_sorteo').css('border','1px solid #C7C7CC');
  }

 if($('#id_transmite').val()==''){
    scrollToID('#id_transmite','#ErrorTransmite','Debe indicar Emisora que Transmite');
    return false;
  }else{
    ErrorHide('#ErrorTransmite');
    $('#id_transmite').css('border','1px solid #C7C7CC');
  }

 
 if($('#id_precio').val()==''){
    scrollToID('#id_precio','#ErrorPrecio','Debe indicar Precio del carton');
    return false;
  }else{
    ErrorHide('#ErrorPrecio');
    $('#id_precio').css('border','1px solid #C7C7CC');
  }

   var formData = new FormData();
  formData.append('fecha',$('#id_fecha').val());
  formData.append('organiza',$('#id_organiza').val());
  formData.append('sorteo',$('#id_sorteo').val());
  formData.append('precio',$('#id_precio').val());
  formData.append('transmite',$('#id_transmite').val());
  formData.append('premio_1',$('#id_premio_1').prop('checked'));
  formData.append('premio_2',$('#id_premio_2').prop('checked'));
  formData.append('premio_3',$('#id_premio_3').prop('checked'));
  formData.append('premio_4',$('#id_premio_4').prop('checked'));
  formData.append('premio_5',$('#id_premio_5').prop('checked'));
  formData.append('premio_6',$('#id_premio_6').prop('checked'));
  formData.append('premio_7',$('#id_premio_7').prop('checked'));
  formData.append('monto_1',$('#id_monto_1').val());
  formData.append('monto_2',$('#id_monto_2').val());
  formData.append('monto_3',$('#id_monto_3').val());
  formData.append('monto_4',$('#id_monto_4').val());
  formData.append('monto_5',$('#id_monto_5').val());
  formData.append('monto_6',$('#id_monto_6').val());
  formData.append('monto_7',$('#id_monto_7').val());
  formData.append('condiciones',$('#id_condiciones').val());
  formData.append('t1f',$('#id_t1f').val());
  formData.append('t1l',$('#id_t1l').val());
  formData.append('t2f',$('#id_t2f').val());
  formData.append('t2l',$('#id_t2l').val());
  formData.append('t3f',$('#id_t3f').val());
  formData.append('t3l',$('#id_t3l').val());
  formData.append('lineasEnJuego',$('#id_lineasEnJuego').val());
  formData.append('cartonBlank',$('#id_cartonBlank').val());
  formData.append('csrfmiddlewaretoken', $("input[name='csrfmiddlewaretoken']").val());
   if($('#id_thumb').val()!=""){
    formData.append('thumb', $('#id_thumb')[0].files[0]);
  }
 
  $.ajax({
           type: "POST",
           url: '/partida/crear/',
           enctype: 'multipart/form-data',         
           data: formData, // serializes the form's elements.
           processData: false,  // tell jQuery not to process the data
           contentType: false,  // tell jQuery not to set contentType           
          success: function(data)
           {

             if(data=='ok'){
                  location.href='/partida/';

              }
           }
         });
  event.preventDefault();
});

/**** ENVIAR AJAX DE Editar PARTIDA ****/
$( "#editPartida" ).submit(function( event ) {



if($('#id_fecha').val()==''){
    scrollToID('#id_fecha','#ErrorFecha','Debe indicar la Fecha');
    return false;
  }else{
    ErrorHide('#ErrorFecha');
    $('#id_fecha').css('border','1px solid #C7C7CC');
  }


if($('#id_organiza').val()==''){
    scrollToID('#id_organiza','#ErrorOrganiza','Debe indicar al Organizador');
    return false;
  }else{
    ErrorHide('#ErrorOrganiza');
    $('#id_organiza').css('border','1px solid #C7C7CC');
  }

 if($('#id_sorteo').val()==''){
    scrollToID('#id_sorteo','#ErrorSorteo','Debe indicar al Dia y Hora del Sorteo');
    return false;
  }else{
    ErrorHide('#ErrorSorteo');
    $('#id_sorteo').css('border','1px solid #C7C7CC');
  }

 if($('#id_transmite').val()==''){
    scrollToID('#id_transmite','#ErrorTransmite','Debe indicar Emisora que Transmite');
    return false;
  }else{
    ErrorHide('#ErrorTransmite');
    $('#id_transmite').css('border','1px solid #C7C7CC');
  }

 
 if($('#id_precio').val()==''){
    scrollToID('#id_precio','#ErrorPrecio','Debe indicar Precio del carton');
    return false;
  }else{
    ErrorHide('#ErrorPrecio');
    $('#id_precio').css('border','1px solid #C7C7CC');
  }

   var formData = new FormData();
  formData.append('id',$('#id_id').val());
  formData.append('fecha',$('#id_fecha').val());
  formData.append('organiza',$('#id_organiza').val());
  formData.append('sorteo',$('#id_sorteo').val());
  formData.append('precio',$('#id_precio').val());
  formData.append('transmite',$('#id_transmite').val());
  formData.append('premio_1',$('#id_premio_1').prop('checked'));
  formData.append('premio_2',$('#id_premio_2').prop('checked'));
  formData.append('premio_3',$('#id_premio_3').prop('checked'));
  formData.append('premio_4',$('#id_premio_4').prop('checked'));
  formData.append('premio_5',$('#id_premio_5').prop('checked'));
  formData.append('premio_6',$('#id_premio_6').prop('checked'));
  formData.append('premio_7',$('#id_premio_7').prop('checked'));
  formData.append('monto_1',$('#id_monto_1').val());
  formData.append('monto_2',$('#id_monto_2').val());
  formData.append('monto_3',$('#id_monto_3').val());
  formData.append('monto_4',$('#id_monto_4').val());
  formData.append('monto_5',$('#id_monto_5').val());
  formData.append('monto_6',$('#id_monto_6').val());
  formData.append('monto_7',$('#id_monto_7').val());
  formData.append('condiciones',$('#id_condiciones').val());
  formData.append('t1f',$('#id_t1f').val());
  formData.append('t1l',$('#id_t1l').val());
  formData.append('t2f',$('#id_t2f').val());
  formData.append('t2l',$('#id_t2l').val());
  formData.append('t3f',$('#id_t3f').val());
  formData.append('t3l',$('#id_t3l').val());
  formData.append('lineasEnJuego',$('#id_lineasEnJuego').val());
  formData.append('cartonBlank',$('#id_cartonBlank').val());
  formData.append('csrfmiddlewaretoken', $("input[name='csrfmiddlewaretoken']").val());
   if($('#id_thumb').val()!=""){
    formData.append('thumb', $('#id_thumb')[0].files[0]);
  }
 
  $.ajax({
           type: "POST",
           url: '/partida/editar/' + $('#id_id').val() + '/',
           enctype: 'multipart/form-data',         
           data: formData, // serializes the form's elements.
           processData: false,  // tell jQuery not to process the data
           contentType: false,  // tell jQuery not to set contentType           
          success: function(data)
           {

             if(data=='ok'){
                  setTimeout("location.href='/partida/'", 300);

              }else{
                alert(data);
              }
           }
         });
  event.preventDefault();
});


//BORRAR ITEM //
function BorrarPartida(id,csrf_token){

 if (confirm('¿Estas seguro de eliminar esta Partida?')) {
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

function generarExcel(){
 
 alert('0');

}