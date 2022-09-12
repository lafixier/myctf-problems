import hashlib
import secrets

from flask import Flask, render_template, request, redirect, url_for, session


HASHED_USERNAME = "c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec"
HASHED_PASSWORD = "f453fa5ec85966c26a05102260cbbb7d72705d7a6c50f372825ffb3a645a624d4ce14a2b590a645fbe6df9291db1422fcd7fa64171f1ed9b745f82a2a9177743"
FLAG = ""
with open("flag.txt", "r") as f:
    FLAG = f.read()

assert FLAG != ""

app = Flask(__name__)
app.secret_key = secrets.token_bytes(512)


def sha512(src: str) -> str:
    return hashlib.sha512(src.encode()).hexdigest()


@app.route("/")
def index_():
    if session.get("user_name"):
        return render_template("index.html", username=session["user_name"], flag=FLAG)
    return redirect(url_for("login_"))


@ app.route("/login", methods=["GET", "POST"])
def login_():
    if request.method == "GET":
        return render_template("login.html")
    else:
        user_name = request.form.get("user_name")
        password = request.form.get("password")
        if user_name and password:
            if sha512(user_name) == HASHED_USERNAME and sha512(password) == HASHED_PASSWORD:
                session["user_name"] = user_name
                return redirect(url_for("index_"))
            return render_template("login.html", message="Invalid username or password.")
        else:
            return render_template("login.html", message="Please enter your user name and password.")


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
