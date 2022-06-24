
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

/**** ENVIAR AJAX DE CREAR SALA ****/
$( "#addSala" ).submit(function( event ) {
if($('#id_nombre').val()==''){
    scrollToID('#id_nombre','#ErrorNombre','Debe ingresar el Nombre');
    return false;
  }else{
    ErrorHide('#ErrorNombre');
    $('#id_nombre').css('border','1px solid #C7C7CC');
  }


if($('#id_direccion').val()==''){
    scrollToID('#id_direccion','#ErrorDireccion','Debe ingresar la direccion');
    return false;
  }else{
    ErrorHide('#ErrorDireccion');
    $('#id_direccion').css('border','1px solid #C7C7CC');
  }


  var formData = new FormData();
  formData.append('nombre',$('#id_nombre').val());
  formData.append('direccion',$('#id_direccion').val());
  formData.append('csrfmiddlewaretoken', $("input[name='csrfmiddlewaretoken']").val());
   if($('#id_thumb').val()!=""){
    formData.append('file', $('#id_thumb')[0].files[0]);
  }
 

   $.ajax({
           type: "POST",
           url: '/salas/crear/',
           enctype: 'multipart/form-data',         
           data: formData, // serializes the form's elements.
           processData: false,  // tell jQuery not to process the data
           contentType: false,  // tell jQuery not to set contentType           
           success: function(data)
           {

             if(data=='ok'){
                  setTimeout("location.href='/salas/'", 300);
              }else if(data == 'salaExiste'){
                  scrollToID('#id_nombre','#ErrorNombre','El Nombre de Sala Registrado');
              }
           }
         });
  return false;
});



/**** ENVIAR AJAX DE EDITAR SALA ****/
$( "#editSala" ).submit(function( event ) {

if($('#id_nombre').val()==''){
    scrollToID('#id_nombre','#ErrorNombre','Debe ingresar el Nombre');
    return false;
  }else{
    ErrorHide('#ErrorNombre');
    $('#id_nombre').css('border','1px solid #C7C7CC');
  }


if($('#id_direccion').val()==''){
    scrollToID('#id_direccion','#ErrorDireccion','Debe ingresar la Dirección');
    return false;
  }else{
    ErrorHide('#ErrorDireccion');
    $('#id_direccion').css('border','1px solid #C7C7CC');
  }


  var formData = new FormData();
  formData.append('nombre',$('#id_nombre').val());
  formData.append('direccion',$('#id_direccion').val());
  formData.append('csrfmiddlewaretoken', $("input[name='csrfmiddlewaretoken']").val());
   if($('#id_thumb').val()!=""){
    formData.append('file', $('#id_thumb')[0].files[0]);
  }
 

   $.ajax({
           type: "POST",
           url: '/salas/editar/' + $('#id_id').val() + '/',
           enctype: 'multipart/form-data',         
           data: formData, // serializes the form's elements.
           processData: false,  // tell jQuery not to process the data
           contentType: false,  // tell jQuery not to set contentType           
           success: function(data)
           {

             if(data=='ok'){
                  setTimeout("location.href='/salas/'", 300);
              }
           }
         });
  return false;
});




//BORRAR ITEM //


function BorrarSala(id,csrf_token){

 if (confirm('¿Estas seguro de eliminar esta Sala?')) {
           $.ajax({
                   type: "POST",
                   url: '/salas/eliminar/' + id + '/',
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


function EstadoSala(id,csrf_token){

 if (confirm('¿Estas seguro de cambiar el estado de esta Sala?')) {
           $.ajax({
                   type: "GET",
                   url: '/salas/estado/?pk=' + id ,
                   data: { 'pk' : id,'csrfmiddlewaretoken': csrf_token },

                   success: function(data)
                   {
                     location.reload();
                   }
                 });
    }
    return false;
}


