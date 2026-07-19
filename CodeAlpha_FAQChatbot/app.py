from flask import Flask
from flask import render_template
from flask import request
from chatbot import FAQChatbot

app = Flask(__name__)

bot = FAQChatbot()


@app.route("/")

def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])

def chat():

    user = request.form["message"]

    response = bot.get_response(user)

    return response


if __name__ == "__main__":
    app.run(debug=True)
