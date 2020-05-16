from flask import request, render_template, redirect
# from core.dialog.manager import DialogManger
from core.nlp.engine import NLPEngine
from extensions import (
    FB_VERIFY_TOKEN,
    LOGGER
)
# from connector.telegram.bot import Bot as Telegram_Bot
from app import app

engine = NLPEngine()

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    elif request.method == 'POST':
        print(request.form['data'])
        response, _, _ = engine.detect_intent_texts(0, request.form['data'], 'en')
        print(response)
        return response
