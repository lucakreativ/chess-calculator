from flask import Flask, request, session, redirect, render_template


app=Flask(__name__)
app.secret_key="sicher"



@app.route("/")
def home():
    if check_login()==False:
        return redirect("/login")
    else:
        return("Hallo "+session["user"])


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/validate", methods=["POST"])
def validate():
    username=request.form.get("username")
    password=request.form.get("password")
    if check_data(username, password):

        session["login"]=2
        session["user"]=username

        return redirect("/")
    else:
        return redirect("/loginf")


def check_data(username, password):
    if username=="luca" and password=="1234":
        return True
    else:
        return False


def check_login():
    if session.get("login")==2:
        return True
    else:
        return False


app.run(host="0.0.0.0", port=5000)