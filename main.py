from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

form = """


"""



@app.route("/user-signup")
def index():

    return render_template('the_form.html')
   





@app.route('/user-signup', methods=['POST'])
def validate_form():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    user_error = ''
    password_error = ''
    verify_password_error = ''
    email_error = ''

    if username == '':
        user_error = "not a valid username. Please enter a username between 3-20 characters"
        return render_template("the_form.html", user_error= user_error ) 
   

    elif (len(username) < 3 ) or (len(username) > 20):
        user_error = "not a valid username. Please enter a username between 3-20 characters"
        username = ""
        return render_template("the_form.html", user_error= user_error, username = username) 

    else:
            
        if ' ' in username:
           user_error = "not a valid username. There can be no spaces within your username and it must be between 2-20 characters"
           username = ""
           return render_template("the_form.html", user_error = user_error, username = username)
   
    if password or verify_password == '':
        password_error = "Not a valid password. Please enter a password between 3-20 characters"
        verify_password_error ="Passwords don't match. Please try again."
        return render_template("the_form.html", password_error= password_error, verify_password_error = verify_password_error) 
        
    else:

        if (len(password) < 3 ) or (len(password) > 20):
            password_error = "not a valid username. Please enter a password that is between 3-20 characters"
            password = ""
            return render_template("the_form.html", password_error= password_error, password = password) 

        else:
            
             if ' ' in password:
                    password_error = "not a valid password. There can be no spaces within your password and it must be between 2-20 characters"
                    password = ""
                    return render_template("the_form.html", password_error= password_error, password=password) 
            
            
            
        if verify_password != password:
                verify_password_error = "not a valid password. Please enter a password that is between 3-20 characters and that matches the previous password entered!"
                verify_password = ""
                return  render_template("the_form.html", verify_password_error= verify_password_error, verify_password = verify_password) 
        
        if "@" not in email:
            email_error = "not a valid email. Please enter an email that contains the @ character."
            email = ''
            return render_template("the_form.html", email_error= email_error, email = email) 
        else:

            if (len(email) < 3 ) or (len(email) > 20):
                email_error = "not a valid email. Please enter an email between 3-20 characters"
                email = ""
                return render_template("the_form.html", email_error= email_error, email = email) 

            else:
            
                if ' ' in email:
                    email_error = "not a valid email. There can be no spaces within your email and it must be between 2-20 characters"
                    email = ""
                    return render_template("the_form.html", email_error = email_error, email = email)
                
               
   
   
   
   
   
   
   





  

app.run()