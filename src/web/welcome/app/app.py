from flask import Flask, render_template


app = Flask(__name__)
FLAG = ""
with open("flag.txt") as f:
    FLAG = f.read()

assert FLAG != ""


@app.route("/")
def index_():
    return render_template("index.html", flag=FLAG)


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
