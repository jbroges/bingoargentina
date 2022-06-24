from django.core.mail import EmailMultiAlternatives

def EnviarEmailDef(titulo,msj,html,email):
	subject, from_email, to = titulo, 'Bingos Marvel<jbroges@gmail.com>', email 
	msg = EmailMultiAlternatives(subject, msj, from_email, [to])
	msg.attach_alternative(html, "text/html")
	msg.send()

