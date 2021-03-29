#Link do Video -> https://www.youtube.com/watch?v=qfOgihp-gEU

#NOTA: A menssagem não pode conter acentos

#Módulos
from tkinter import *
import smtplib

#Criar a janela
master = Tk()
#Cor de fundo da janela
master.configure(background='black')
#Titulo da janela
master.title('Email App')

#Função Enviar
def send():
    try: 
        username = temp_username.get()
        password = temp_password.get()
        to = temp_receiver.get()
        subject = temp_subject.get()
        body = temp_body.get()
        #Se faltar preencher algum campo
        if username=="" or password=="" or to=="" or subject=="" or body=="":
            #Irá mostrar a mensagem
            notif.config(text="É necessário preencher todos os campos", fg="red")
            return
        #Se todos os campos forem preenchidos
        else:
            #Message
            finalMessage = 'Subject: {}\n\n{}'.format(subject, body)
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            #Login
            server.login(username, password)
            #Enviar o email
            server.sendmail(username,to,finalMessage)
            #Notificação de que o email foi enviado com sucesso
            notif.config(text="Email enviado com sucesso", fg="green")
    except:
        #Se ocurrer algum problema no envio da mensagem irá aparecer a mensagem de Erro
        #Por exemplo dados de login incorretos
        notif.config(text="Erro ao enviar o email", fg="red")

#Função Reset - Limpa todos os campos
def reset():
  usernameEntry.delete(0,'end')
  passwordEntry.delete(0,'end')
  receiverEntry.delete(0,'end')
  subjectEntry.delete(0,'end')
  bodyEntry.delete(0,'end')

#Labels
#Titulo
Label(master, text="Email App", font=('Calibri',15),background='black',foreground="white").grid(row=0, sticky=N)
#Subtitulo
Label(master, text="Please use the form below to send an email", font=('Calibri',11),background='black',foreground="white").grid(row=1, sticky=W, padx=5 ,pady=10)
#Texto que apareçe atrás das TextBoxs
Label(master, text="Email", font=('Calibri', 11),background='black',foreground="white").grid(row=2,sticky=W, padx=5)
Label(master, text="Password", font=('Calibri', 11),background='black',foreground="white").grid(row=3,sticky=W, padx=5)
Label(master, text="To", font=('Calibri', 11),background='black',foreground="white").grid(row=4,sticky=W, padx=5)
Label(master, text="Subject", font=('Calibri', 11),background='black',foreground="white").grid(row=5,sticky=W, padx=5)
Label(master, text="Message", font=('Calibri', 11),background='black',foreground="white").grid(row=6,sticky=W, padx=5)
#Notificação
notif = Label(master, text="", font=('Calibri', 11),background='black',fg="red")
notif.grid(row=7,sticky=S)

#Storage - Variavéis que vão atuar como um armazenamento
temp_username = StringVar()
temp_password = StringVar()
temp_receiver = StringVar()
temp_subject = StringVar()
temp_body = StringVar()

#TextBoxs
#TextBox Username
usernameEntry = Entry(master, textvariable = temp_username)
usernameEntry.grid(row=2,column=0)
#TextBox Password - O show="*" permite que quando escrevermos a palvra passa apenas se veja *
passwordEntry = Entry(master, show="*", textvariable = temp_password)
passwordEntry.grid(row=3,column=0)
#TextBox To
receiverEntry = Entry(master, textvariable = temp_receiver)
receiverEntry.grid(row=4,column=0)
#TextBox Subject - Assunto
subjectEntry = Entry(master, textvariable = temp_subject)
subjectEntry.grid(row=5,column=0)
#TextBox Message
bodyEntry = Entry(master, textvariable = temp_body)
bodyEntry.grid(row=6,column=0)

#Buttons
#Button Enviar
Button(master, text = "Send", command = send).grid(row=7,sticky=W,pady=15,padx=5)
#Button Reset
Button(master, text = "Reset", command = reset).grid(row=7,sticky=W,padx=45,pady=40)

#Mainloop - Inicializar a janela
master.mainloop()