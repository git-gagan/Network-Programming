import smtplib
#Standard library, defines an smtp client session object, used to send mail
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP("smtp.gmail.com",587)
#returns an object and manages a connection to smtp server

#server.ehlo()
server.starttls()
#fun to identify the server

with open("Pass.txt") as f:
    password = f.read()
server.login("sender@gmail.com",password) #using app password to overcome 2 factor auth
with open("Content.txt") as f:
    content = f.read()

recipient = "receiver@gmail.com"
sender = "sender@gmail.com"
#sending an image using MIME
msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = recipient
msg["Subject"] = "Automated Email Testing"

#to attach a subpart to the MIME message, use .attach()
msg.attach(MIMEText(content))
file = "download.jpg"
pic = open(file,"rb")

p = MIMEBase("application","octet-stream")
p.set_payload(pic.read())
encoders.encode_base64(p)
p.add_header("content-disposition",f'attachment; filename = {file}') #Strictly follow

msg.attach(p)
msg = msg.as_string()

server.sendmail(sender,recipient,msg)

