#Enviar email, Anexo e Assunto (Gmail)

#Módulos
import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders

#Informações
#Nome do ficheiro
file = 'Excel.xlsx'
#Email
username = 'testes.programacao.teste@gmail.com'
#Palavra Passe
password = 'testes1234'
#Objeto 
msg = MIMEMultipart()
#Remetente
msg['From'] = username
#Destinatário
msg['To'] = username
#Assunto
msg['Subject'] = 'Python'

#Diretório
smtp = smtplib.SMTP('smtp.gmail.com')
#Porta do gmail
port = '587'

#Anexo
#Abrir o Anexo
fp = open(file, 'rb')
#Indicação do tipo de ficheiro
part = MIMEBase('application','vnd.ms-excel')
#Ler o Anexo
part.set_payload(fp.read())
#Fechar 
fp.close()
#Define o cabeçalho mas não é visivel pelas pessoas
encoders.encode_base64(part)
#Indicação do ficheiro
part.add_header('Content-Disposition', 'attachment', filename=file)
#Juntar o ficheiro ao email
msg.attach(part)
#Indico o comando de protocolo starttls que tem a ver com a criptografia (Escrita no computador) no email 
smtp.starttls()

#Login
smtp.login(username,password)
#Enviar o email
smtp.sendmail(username, username.split(','), msg.as_string())

#Fechar
smtp.quit()