
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

/**** ENVIAR AJAX DE CREAR USUARIO ****/
$( "#configform" ).submit(function( event ) {

if($('#id_tiempoMaster').val()==''){
    scrollToID('#id_tiempoMaster','#ErrortiempoMaster','Debe ingresar un numero igual o mayor a 5000 para un buen funcionamiento');
    return false;
  }else{
    ErrorHide('#ErrortiempoMaster');
    $('#id_tiempoMaster').css('border','1px solid #C7C7CC');
  }

  if($('#id_tiempoInter').val()==''){
    scrollToID('#id_tiempoInter','#ErrortiempoInter','Debe ingresar un numero igual o mayor a 3000 para un buen funcionamiento');
    return false;
  }else{
    ErrorHide('#ErrortiempoInter');
    $('#id_tiempoInter').css('border','1px solid #C7C7CC');
  }

   $.ajax({
           type: "POST",
           url: '/configuracion/1/',
           data: $( "#configform").serialize(), // serializes the form's elements.
           success: function(data)
           {

              if(data=='existeDNI'){
                scrollToID('#id_dni','#Errordni','Este D.N.I. esta Registrado');             
              }else if(data=='ok'){
                  setTimeout("location.href='/configuracion/1/'", 500);
              }
           }
         });
  event.preventDefault();
});

