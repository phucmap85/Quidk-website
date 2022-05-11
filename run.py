from curses import flash
from flask import Flask, render_template, url_for
import json
from transformers import pipeline
from bs4 import BeautifulSoup
import requests
import googletrans
from googletrans import Translator

app = Flask(__name__);

summarizer = pipeline("summarization")

def LongFormSummarize(Text):
    translator = Translator()
    translated = translator.translate(Text, dest='en')
    res = summarizer(translated, max_length=200, min_length=30, do_sample=False)
    final_com = ' '.join([summ['summary_text'] for summ in res])
    pp = translator.translate(final_com, dest=translator.detect(Text)[0].lang)
    return pp.text;

@app.route("/")
def first():
    return page1();

@app.route("/home")
def page1():
    return render_template('home.html')

@app.route('/home/<string:userInput>', methods=['POST'])
def get(userInput):
    userInput = json.loads(userInput);
    return LongFormSummarize(userInput['text']);

@app.route("/linkemb")
def page2():
    return render_template('linkemb.html')

if __name__ == "__main__":
    app.run(debug = True);