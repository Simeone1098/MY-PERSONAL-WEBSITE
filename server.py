import smtplib
from flask import Flask, render_template, send_file, request, redirect, url_for
import requests
import os

app = Flask(__name__)

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇



API_URL = os.getenv("API_URL")
OWN_EMAIL = os.getenv("OWN_EMAIL")
OWN_PASSWORD = os.getenv("OWN_PASSWORD")

posts = requests.get(API_URL).json()
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/asset/curriculum.pdf")
def curriculum():
    return send_file("static/curriculum.pdf", as_attachment=True)


@app.route("/explore")
def explore_asset():
    return render_template("explore_asset.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["message"])
        # return redirect(url_for("success"))
        return redirect(url_for("success"))
    return render_template("index.html", msg_sent=False)


def send_email(name, email, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:  # Explicitly specify port
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)


@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
