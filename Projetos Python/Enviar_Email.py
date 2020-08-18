#Enviar email, mensagem de texto (Gmail)

#Módulos
import smtplib

#Email
email = input(str("Insira o seu email: "))
#Palavra Passe
password = input(str("Insira a sua palavra passe: "))
#Mensagem desejada
message = input(str("Escreva a mensagem que deseje enviar (Não pode conter acentos): "))

#Indicamos o tipo de email neste caso gmail e a porta
server = smtplib.SMTP('smtp.gmail.com', 587)
#Indico o comando de protocolo starttls que tem a ver com a criptografia (Escrita no computador) no email 
server.starttls()
#Indicamos o email e a palavra passe
server.login(email, password)
#Menssagem para verificar que o login foi executado corretamente
print("Login executado")
#Endicamos quem vai enviar a mensagem, que vai receber a menssagem e a mensagem
server.sendmail(email, email, message)
#Menssagem para verificar que o eemail foi enviado com exito
print("Email enviado com exito para:", email)