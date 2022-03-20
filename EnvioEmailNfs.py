import smtplib
from email import encoders
from email.mime.base import MIMEBase

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
port = "587"
login = ""
senha = ""
destinatario = ""

server = smtplib.SMTP(host,port)

server.ehlo()
server.starttls()
server.login(login,senha)

corpo = """ Ola Tudo bom ?

<p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s. </> 

<p>Abs</p>
<p> Rafael Santos </>


"""

email_msg = MIMEMultipart()
email_msg['From'] = login
email_msg['To'] = destinatario
email_msg['Subject'] = "Meu e-mail enviado por Rafael"
email_msg.attach(MIMEText(corpo,'html'))

#Lendo Binario do Arquivo a ser Anexado
cam_arquivo_1 = "/home/rafael/Documentos/nfs_bot/Rafael_Santos_De_Araujo_Boleto.pdf"
attchment = open(cam_arquivo_1,'rb')

att = MIMEBase('application', 'octet-stream')
att.set_payload(attchment.read())
encoders.encode_base64(att)

att.add_header('Content-Disposition', f'attachment; filename = Rafael_Santos_De_Araujo_Boleto.pdf')
attchment.close()
email_msg.attach(att)

server.sendmail(email_msg['From'],email_msg['To'],email_msg.as_string())
server.quit()