from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

form = """


"""



@app.route("/")
def index():
    template = jinja_env.get_template('the_form.html')
    return template.render()

@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    template = jinja_env.get_template9'hello_greeting.html')
    return template.render(name=firstname)


@app.route("/validate-signup")
def display_form():
    return the_form.format(email='', username='', password='', verify_password='', 
    user_error='', password_error='', verify_password_error='', email_error='' )


def is_int_or_str(num):
    try:
        int(num) or str(num)
        return True
    except ValueError:
        return False

@app.route('/validate-signup', methods=['Post'])
def validate_form():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.email['email']

    user_error = ''
    password_error = ''
    verify_password_error = ''

    if not is_int_or_str(username):
        user_error = 'Not a valid user'

    if not is_int_or_str(password):
        password_error = "not a valid password"

    if not is_int_or_str(verify_password):
        verify_password_error = 'Not a valid verification'
    if not is_int_or_str(email):
        email_error = 'Not a valid email'

    else:
        template = jinja_env.get_template('the_form.html')
        return template.render(user_error=user)error, password_error=password_error, 
        verify_password_error=verify_password_error, email_error=email_error, username=username, password=password, email=email)

app.run()