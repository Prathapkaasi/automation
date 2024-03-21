import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl


def send_mail():
    sender_mail = 'prathapkaasi@gmail.com'
    receiver_mail = 'sonasri16495@gmail.com'
    password = "aoscmkmdbujwruhu"
    message = MIMEMultipart()
    message["To"]=receiver_mail
    message["From"] = sender_mail
    message["Subject"] = "Hey There! Wake Up! Your Birthday Here Da! Venna Mavane😁"

    body = """
    Thank for being the most loving and caring brother in entire wolrd.\n
    No one understand me better than u. \n
    
முழு உலகிலும் மிகவும் அன்பான மற்றும் அக்கறையுள்ள சகோதரனாக இருப்பதற்கு நன்றி.
    உன்னை விட யாரும் என்னை நன்றாக புரிந்து கொள்ள மாட்டார்கள்.\n
    ❤️❤️❤️Wishing You Memorable Happiest Birthday🎂🎂🎂 
    """
    message.attach(MIMEText(body,"plain"))

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host="smtp.gmail.com",port=465,context=context) as server:
        server.login(sender_mail, password)
        server.sendmail(from_addr=sender_mail, to_addrs=receiver_mail,msg=message.as_string())
    print("sent!")


