from flask import request, url_for, render_template, Flask
from werkzeug.utils import redirect

from email_sender import send_mail

app = Flask(import_name='main', template_folder='templates')


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    username_error = None
    password_error = None
    if request.method == 'POST':
        data = request.form
        username = data['username']
        password = data['password']
        # Check if username equals admin
        correct_username = 'admin'
        correct_pass = '123'

        # Check if username equals admin
        if username != correct_username:
            username_error = 'Invalid username ' + username
        # Check if password equals admin
        if password != correct_pass:
            password_error = 'Wrong password '

        if username == correct_username and password == correct_pass:
            return redirect(url_for('email'))
        # if user correct and pass correct return redirect(url_for('email'))

    return render_template('login.html', username_error=username_error, password_error=password_error)


@app.route('/email', methods=['GET', 'POST'])
def email():
    email_error = None
    subject_error = None
    message = None
    if request.method == 'POST':
        data = request.form
        email = data['email']
        subject = data['subject']
        email_password = data['email_password']
        email_message = data['message']
        # Check if email is empty and set error message
        if email == "":
            email_error = 'Please enter valid e-mail.'
        # Check if subject is empty and set error message
        if subject == "":
            subject_error = 'Please enter non-empty subject'
        # Check if credentials are provided
        if email != "" and email_password != "":
            send_mail(email, email_password, subject, email_message)
            return render_template('email.html', email_error = None, subject_error = None, message = 'Email sent successfully')
        else:
            message = "Please enter e-mail credentials"
        # if provided:
        # send_mail(email, email_password, subject, email_message)
        # return render_template('email.html', email_error=None, subject_error=None, message='Email sent successfully')
        # if not provided:
        # set error message

    return render_template('email.html', email_error=email_error, subject_error=subject_error, message=message)


if __name__ == '__main__':
    app.run(port=7000)
