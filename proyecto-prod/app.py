from flask import Flask,render_template,request,flash
from py.gmail import envio_correo
import os,urllib.parse,webbrowser
from py.messages import MESSAGE_TYPE

app = Flask(__name__)
app.secret_key = os.getenv('API_KEY')

@app.route('/', methods=['GET','POST'])
def home():
    return render_template('index.html')


@app.route('/envio_correo', methods=['POST'])
def send_email_view():
    sender_name = request.form['sender_name']
    sender_email = request.form['sender_email']
    asunto = request.form['subject']
    message = request.form['message']
    if request.form.get('envio_window') == MESSAGE_TYPE.WINDOWS:
        # Formatear los datos para el enlace "mailto"
        to = "web.ncastro@correo.com"
        subject = "{}".format(asunto)
        body = "Enviado por: {}\nCorreo electrónico: {}\n{}\n{}\n".format(sender_name, sender_email,subject, message)
        headers = "From: {} <{}>\r\nReply-To: {}\r\nContent-type: text/plain; charset=UTF-8".format(sender_name, sender_email, sender_email)

        mailto_link = "mailto:{}?subject={}&body={}&headers={}".format(to, urllib.parse.quote(subject), urllib.parse.quote(body), urllib.parse.quote(headers))
        webbrowser.open(mailto_link)
        return render_template('confirm.html')
    if request.form.get('envio_gmail') == MESSAGE_TYPE.GMAIL:
        enviado = envio_correo(sender_name,sender_email,asunto,message)
        if enviado:
            confirmation_message = "Correo enviado correctamente"   
        else:
            confirmation_message = "Error al enviar el correo"
    return render_template('confirm.html', confirmation_message=confirmation_message)


if __name__ == "__main__":
    app.run(debug=True)
