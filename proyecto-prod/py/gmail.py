import os,base64
from dotenv import load_dotenv
from py.Google import Create_Service
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
from py.directory import searchDirectory

load_dotenv()

def envio_correo(sender_name,sender_email,subject,message):
    TOKENS_DIR = searchDirectory('tokens')
    CLIENT_SECRET_FILE = TOKENS_DIR + "token.json"
    print(CLIENT_SECRET_FILE)
    API_NAME = "gmail"
    API_VERSION = "v1"
    SCOPES = ["https://mail.google.com/"]

    # obtiene las credenciales desde el archivo .env
    email_sender = os.getenv("EMAIL_USERNAME")
    email_password = os.getenv("EMAIL_PASSWORD")
    try:
        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES, email_sender, email_password)   
        # Cargar la plantilla HTML
        TEMPLATES_DIR = searchDirectory('templates')
        env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))
        template = env.get_template('plantilla_correo.html')
        # Definir las variables para la plantilla
        html = template.render(sender_name=sender_name,sender_email=sender_email,subject=subject, message=message)
        # crear mensaje
        mimeMessage = MIMEMultipart()
        mimeMessage["to"] = "web.ncastro@gmail.com"
        mimeMessage["subject"] = subject
        mimeMessage.attach(MIMEText(html, "html"))
        # Codificar el mensaje MIME en base64 y enviarlo
        raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
        message = service.users().messages().send(userId="me", body={"raw": raw_string}).execute()
        return True
    except NameError:
        return False
    
