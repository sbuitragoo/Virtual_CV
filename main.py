from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("main", usr=user))
    else:
        return render_template("index.html")


@app.route("/main/<usr>", methods=["POST", "GET"])
def main(usr):
    return render_template("main.html", name=usr)

if __name__ == "__main__":
    app.run(debug=True)
