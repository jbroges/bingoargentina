
/**** SETTINGS AJAX ****/

    $(document).ajaxStart(function() {
        $('#btn-Entrar').html('<img src="http://dockrealty.biz/images/preloader2.gif" width="32px">');
        $('#btn-Entrar').attr('disabled','disabled');   
    });
    $(document).ajaxStop(function() {
        $('#btn-Entrar').html('Login');
        $('#btn-Entrar').removeAttr('disabled');
    });



/**** ENVIAR AJAX DE LOGIN ****/
$( "#loginIntForm" ).submit(function( event ) {
	if($('#usuario').val()==''){
    //MENSAJE DE ERROR
    error_msj('Debe Ingresar el Usuario')
    //SE COLOCA ROJO LOS BORDES DE LOS TEXTIS
    $('#icousuario').css('border','1px solid red');
    $('#usuario').css('border','1px solid red');
    $('#icousuario').css('border-right','none');
    $('#usuario').css('border-left','none');
		return false;
	}else if($('#clave').val()==''){
    //MENSAJE DE ERROR
    error_msj('Debe Ingresar el Password')
    //SE COLOCA ROJO LOS BORDES DE LOS TEXTIS
    $('#usuario').css('border','none');
    $('#icousuario').css('border','none');
    $('#icoclave').css('border','1px solid red');
    $('#clave').css('border','1px solid red');
    $('#icoclave').css('border-right','none');
    $('#clave').css('border-left','none');

		return false;
	}


   $.ajax({
           type: "POST",
           url: '/usuario/login/',
           data: $("#loginIntForm").serialize(), // serializes the form's elements.
           success: function(data)
           {
               if(data=='ok'){
               	window.location = '/app/';
               }else{
                  //MENSAJE DE ERROR
                  error_msj(data)
                  //SE COLOCAN ROJOS LOS BORDES DE LOS TEXTOS 
                  $('#icousuario').css('border','1px solid red');
                  $('#usuario').css('border','1px solid red');
                  $('#icousuario').css('border-right','none');
                  $('#usuario').css('border-left','none');
                  $('#icoclave').css('border','1px solid red');
                  $('#clave').css('border','1px solid red');
                  $('#icoclave').css('border-right','none');
                  $('#clave').css('border-left','none');
               }
           }
         });
  event.preventDefault();
});

function error_msj(data){
  $('#mensaje').html(data);
  $('#mjError').fadeIn('slow');

}
