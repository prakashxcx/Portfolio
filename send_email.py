import smtplib, ssl
def send_email(messege):
    host = 'smtp.gmail.com'
    port =  465

    username = 'krishmusic.1436@gmail.com'
    password = ''

    receiver = 'krishmusic.1436@gmail.com'
    context = ssl.create_default_context()
   

    with smtplib.SMTP_SSL(host,port,context=context) as server :
        server.login(username,password)
        server.sendmail(username,receiver,messege)

