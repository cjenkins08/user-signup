from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

form = """

<!Doctype html>
<html>
<header>
    <head>
        <link type="text/css" rel="stylesheet" href="style.css"/>
        <title> User Signup Assignment </title>
    </head>
</header>

<body>
  <form action="text", method ='POST'>
    <label> Username
        <input name="user" value="0" type="text" />
    <label>
    # @todo validate
    
    <br>
    
    <label> Password
        <input name="pass1" value="0" type="text" />
    </label>
    # @todo validate
    
    <br>
    
    <label> Verify Password
        <input name="passver" value="0" type="text" />
    </label>
   # @todo validate
    
    <br>
    <label> Email (optional)
        <input name="email" value="0" type="text" />
        <input> type = "submit" </input>
    </label>
    # @todo validate

</body>
<footer>
    C. Jenkins Assignment 3
</footer>
</html>

"""

@app.route("/")
def index():
    return "form"

app.run()