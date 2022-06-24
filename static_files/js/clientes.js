
$("#id_telefono").on('input', function() {  //this is use for every time input change.
        var inputValue = getInputValue(); //get value from input and make it usefull number
        var length = inputValue.length; //get lenth of input
        if (inputValue < 1000)
        {
            inputValue = '57('+inputValue;
        }else if (inputValue < 1000000) 
        {
            inputValue = '57('+ inputValue.substring(0, 3) + ')' + inputValue.substring(3, length);
        }else if (inputValue < 10000000000) 
        {
            inputValue = '57('+ inputValue.substring(0, 3) + ')' + inputValue.substring(3, 6) + '-' + inputValue.substring(6, length);
        }else
        {
            inputValue = '57('+ inputValue.substring(0, 3) + ')' + inputValue.substring(3, 6) + '-' + inputValue.substring(6, 10);
        }       
        $("#id_telefono").val(inputValue); //correct value entered to your input.
        inputValue = getInputValue();//get value again, becuase it changed, this one using for changing color of input border
       if ((inputValue > 2000000000) && (inputValue < 9999999999))
      {
          $("#id_telefono").css("border","#C7C7CC solid 1px");//if it is valid phone number than border will be black.
      }else
      {
          $("#id_telefono").css("border","red solid 1px");//if it is invalid phone number than border will be red.
      }
  });

    function getInputValue() {
         var inputValue = $("#id_telefono").val().replace(/\D/g,'');  //remove all non numeric character
        if (inputValue.charAt(0) == 5) // if first character is 1 than remove it.
        {
            var inputValue = inputValue.substring(2, inputValue.length);
        }
        return inputValue;
}

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
$( "#addCliente" ).submit(function( event ) {

if($('#id_nombre').val()==''){
    scrollToID('#id_nombre','#ErrorNombre','Debe ingresar el Nombre');
    return false;
  }else{
    ErrorHide('#ErrorNombre');
    $('#id_nombre').css('border','1px solid #C7C7CC');
  }

  if($('#id_apellido').val()==''){
    scrollToID('#id_apellido','#ErrorApellido','Debe ingresar el Apellido');
    return false;
  }else{
    ErrorHide('#ErrorApellido');
    $('#id_apellido').css('border','1px solid #C7C7CC');
  }

  if($('#id_dni').val()==''){
    scrollToID('#id_dni','#Errordni','Debe ingresar el D.N.I.');
    return false;
  }else{
    ErrorHide('#Errordni');
    $('#id_dni').css('border','1px solid #C7C7CC');
  }

  if($('#id_telefono').val()==''){
    scrollToID('#id_telefono','#ErrorTelefono','Debe ingresar el Teléfono');
    return false;
  }else{
    ErrorHide('#ErrorTelefono');
    $('#id_telefono').css('border','1px solid #C7C7CC');
  }

  if($('#id_direccion').val()==''){
    scrollToID('#id_direccion','#ErrorDireccion','Debe ingresar la Dirección');
    $('#id_direccion').css('border','2px solid red');
    return false;
  }else{
    ErrorHide('#ErrorDireccion');
    $('#id_direccion').css('border','1px solid #C7C7CC');
  }


  var formData = new FormData();
  formData.append('dni',$('#id_dni').val());
  formData.append('nombre',$('#id_nombre').val());
  formData.append('apellido',$('#id_apellido').val());
  formData.append('telefono',$('#id_telefono').val());
  formData.append('direccion',$('#id_direccion').val());
  formData.append('sala',$('#id_sala').val());
  formData.append('csrfmiddlewaretoken', $("input[name='csrfmiddlewaretoken']").val());
  if($('#id_thumb').val()!=""){
    formData.append('file', $('#id_thumb')[0].files[0]);
  }
  

   $.ajax({
           type: "POST",
           url: '/cliente/crear/',
           enctype: 'multipart/form-data',         
           data: formData, // serializes the form's elements.
           processData: false,  // tell jQuery not to process the data
           contentType: false,  // tell jQuery not to set contentType           
           success: function(data)
           {

              if(data=='existeDNI'){
                scrollToID('#id_dni','#Errordni','Este D.N.I. esta Registrado');             
              }else if(data=='ok'){
                  setTimeout("location.href='/cliente/'", 500);
              }
           }
         });
  event.preventDefault();
});


/**** ENVIAR AJAX DE CREAR USUARIO ****/
$( "#editCliente" ).submit(function( event ) {

if($('#id_nombre').val()==''){
    scrollToID('#id_nombre','#ErrorNombre','Debe ingresar el Nombre');
    return false;
  }else{
    ErrorHide('#ErrorNombre');
    $('#id_nombre').css('border','1px solid #C7C7CC');
  }

  if($('#id_apellido').val()==''){
    scrollToID('#id_apellido','#ErrorApellido','Debe ingresar el Apellido');
    return false;
  }else{
    ErrorHide('#ErrorApellido');
    $('#id_apellido').css('border','1px solid #C7C7CC');
  }

  if($('#id_dni').val()==''){
    scrollToID('#id_dni','#Errordni','Debe ingresar el D.N.I.');
    return false;
  }else{
    ErrorHide('#Errordni');
    $('#id_dni').css('border','1px solid #C7C7CC');
  }

  if($('#id_telefono').val()==''){
    scrollToID('#id_telefono','#ErrorTelefono','Debe ingresar el Teléfono');
    return false;
  }else{
    ErrorHide('#ErrorTelefono');
    $('#id_telefono').css('border','1px solid #C7C7CC');
  }

  if($('#id_direccion').val()==''){
    scrollToID('#id_direccion','#ErrorDireccion','Debe ingresar la Dirección');
    $('#id_direccion').css('border','2px solid red');
    return false;
  }else{
    ErrorHide('#ErrorDireccion');
    $('#id_direccion').css('border','1px solid #C7C7CC');
  }


  var formData1 = new FormData();
  formData1.append('dni',$('#id_dni').val());
  formData1.append('nombre',$('#id_nombre').val());
  formData1.append('apellido',$('#id_apellido').val());
  formData1.append('telefono',$('#id_telefono').val());
  formData1.append('direccion',$('#id_direccion').val());
  formData1.append('sala',$('#id_sala').val());
  formData1.append('csrfmiddlewaretoken', $("input[name='csrfmiddlewaretoken']").val());
  if($('#id_thumb').val()!=""){
    formData1.append('file', $('#id_thumb')[0].files[0]);
  }
  

   $.ajax({
           type: "POST",
           url: '/cliente/editar/' +  $('#id_id').val() + '/',
           enctype: 'multipart/form-data',         
           data: formData1, // serializes the form's elements.
           processData: false,  // tell jQuery not to process the data
           contentType: false,  // tell jQuery not to set contentType           
           success: function(data)
           {

            if(data=='ok'){
                  setTimeout("location.href='/cliente/'", 300);
            }
           }
         });
   return false;
});



//BORRAR ITEM //


function BorrarCliente(id,csrf_token){
 if (confirm('¿Estas seguro de eliminar esta Cliente?')) {
           $.ajax({
                   type: "POST",
                   url: '/cliente/eliminar/' + id + '/',
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