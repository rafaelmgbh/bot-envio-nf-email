import smtplib
from email import encoders
from email.mime.base import MIMEBase

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import getpass



host = "smtp.gmail.com"
port = "587"

destinatario = "rafael.santos@dev.simbioseventures.com"

print("**********************************************")
print(" Automação Envio NFs e Boleto Simbiose ")
print("**********************************************")

login = input("Qual seu E-mail: ")
senha = getpass.getpass('Senha:')
salario = int(input("Salário Base : R$ "))
desc_terapia = int(input("Informe o Valor da Terapia : R$  "))
desc_ingles = int(input("Informe o Valor do Ingles : R$  "))

server = smtplib.SMTP(host,port)

server.ehlo()
server.starttls()
server.login(login,senha)

corpo = f""" Ola Tudo bom ?<br>
Segue Boleto , NFs e XML <br>
O Salário Base e de <b>R$ {salario}</b> <br>
Desconto da Terapia  e de R$ {desc_terapia}<br>
Desconto do Ingles e de R$ {desc_ingles}<br>
<br>
<b>O Salário Liquido e de R$ {salario-(desc_terapia+desc_ingles)}</b>
<br><br>
<p>Abs</p>
<p> Rafael Santos </>


"""

email_msg = MIMEMultipart()
email_msg['From'] = login
email_msg['To'] = destinatario
email_msg['Subject'] = "Rafael Santos NFs e BOLETO"
email_msg.attach(MIMEText(corpo,'html'))

#Lendo Binario do Arquivo a ser Anexado
cam_arquivo_1 = "/home/rafael/Documentos/nfs_bot/Rafael_Santos_De_Araujo_Boleto.pdf"
cam_arquivo_2 = "/home/rafael/Documentos/nfs_bot/Rafael_Santos_De_Araujo_NFS.pdf"
cam_arquivo_3 = "/home/rafael/Documentos/nfs_bot/nfse_202200000000002.xml"

attchment = open(cam_arquivo_1,'rb')
att = MIMEBase('application', 'octet-stream')
att.set_payload(attchment.read())
encoders.encode_base64(att)
att.add_header('Content-Disposition', f'attachment; filename = Rafael_Santos_De_Araujo_Boleto.pdf')
attchment.close()
email_msg.attach(att)

attchment = open(cam_arquivo_2,'rb')
att = MIMEBase('application', 'octet-stream')
att.set_payload(attchment.read())
encoders.encode_base64(att)
att.add_header('Content-Disposition', f'attachment; filename = Rafael_Santos_De_Araujo_NFS.pdf')
attchment.close()
email_msg.attach(att)

attchment = open(cam_arquivo_3,'rb')
att = MIMEBase('application', 'octet-stream')
att.set_payload(attchment.read())
encoders.encode_base64(att)
att.add_header('Content-Disposition', f'attachment; filename = nfse_202200000000002.xml')
attchment.close()
email_msg.attach(att)


server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())
server.quit()

print("**********************************************")
print(" NFs e Boleto Enviado com Suceso ! ")
print("**********************************************")
