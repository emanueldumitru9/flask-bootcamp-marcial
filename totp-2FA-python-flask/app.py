from flask import *
from flask_bootstrap import Bootstrap
import pyotp

# configuring flask application
app = Flask(__name__)
app.config["SECRET_KEY"] = "APP_SECRET_KEY"
Bootstrap(app)

# homepage route
@app.route("/")
def index():
    return "<h1> Hello World! </h1>"

# login page route
@app.route("/login", methods=["POST"])
def login_form():
    # demo credentials
    credentials = {"username" : "test", "password" : "password"}
    
    # getting form data
    username = request.form.get("username")
    password = request.form.get("password")
    
    # authenticate submitted credentials with demo credentials
    if username == credentials["username"] and password == credentials["password"]:
        # inform users if credentials are valid
        flash("The credentials provided are valid", "success")
        
        #redirecting users to 2FA page when credentials are valid
        return redirect(url_for("login_2fa"))
    else:
        # inform users if credentials are invalid
        flash("You have supplied invalid login credentials!", "danger")
        return redirect(url_for("login"))
    
@app.route("/login")
def login():
    return render_template("login.html")


# 2FA page route
@app.route("/login/2fa/")
def login_2fa():
    # generating random secret key for authentication
    secret = pyotp.random_base32()
    return render_template("login_2fa.html", secret=secret)


# 2FA form route
@app.route("/login/2fa/", methods = ["POST"])
def login_2fa_form():
    # getting secret key used by user
    secret = request.form.get("secret")
    
    # getting OTP provided by user
    otp = int(request.form.get("otp"))
    
    # verfying submitted OTP with PyOTP
    if pyotp.TOTP(secret).verify(otp):
        
        # inform users if OTP is valid
        flash("The TOTP 2FA token is valid", "success")
        return redirect(url_for("login_2fa"))
    else:
        # inform users if OTP is invalid
        flash("You have supplied an invalid 2FA token!", "danger")
        return redirect(url_for("login_2fa"))
    



# running flask server
if __name__ == "__main__":
    app.run(debug=True)
