from flask import Flask, render_template, request
from transformers import pipeline
from bs4 import BeautifulSoup
import requests
from googletrans import Translator
import docx
import PyPDF2

app = Flask(__name__)

summarizer = pipeline("summarization")

translator = Translator()

# File Summarization
def readDocx(fileName):
    doc = docx.Document(fileName)
    
    completedText = []

    for paragraph in doc.paragraphs:
        completedText.append(paragraph.text)
    
    return '\n'.join(completedText)

# def readPDF(fileName):


def FileSummarize(link, lang, type):
    response = requests.get(link)
    filename = ""
    text = "As travel recovers from pandemic lows, travelers are once again experiencing the consequences of overtourism at enticing, but crowded, destinations. The UN World Tourism Organization, along with public and private sector partners, marks September 27 as World Tourism Day and uses this platform to discuss tourism’s social, political, economic, and environmental impacts."

    if(type == 'docx'):
        filename = "example.docx"
    else:
        filename = "example.pdf"

    open(filename, "wb").write(response.content)
    
    if(type == 'docx'):
        text = readDocx(filename)

    return TextSummarize(text, lang)

# Link Summarization
def LinkSummarize(URL, lang):
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, 'html.parser')
    results = soup.find_all(['h1', 'p'])
    text = [result.text for result in results]
    ARTICLE = ' '.join(text)
    
    max_chunk = 500

    ARTICLE = ARTICLE.replace('.', '.<eos>')
    ARTICLE = ARTICLE.replace('?', '?<eos>')
    ARTICLE = ARTICLE.replace('!', '!<eos>')
    sentences = ARTICLE.split('<eos>')

    current_chunk = 0 
    chunks = []

    for sentence in sentences:
        if len(chunks) == current_chunk + 1: 
            if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
                chunks[current_chunk].extend(sentence.split(' '))
            else:
                current_chunk += 1
                chunks.append(sentence.split(' '))
        else:
            chunks.append(sentence.split(' '))

    for chunk_id in range(len(chunks)):
        chunks[chunk_id] = ' '.join(chunks[chunk_id])

    translated = translator.translate(chunks, dest='en')
    final_text = [trans.text for trans in translated]
    res = summarizer(final_text, max_length=200, min_length=30, do_sample=False)
    final_com = ' '.join([summ['summary_text'] for summ in res])
    if(lang == "en"):
        return final_com
    else:
        pp = translator.translate(final_com, dest=lang)
        return pp.text

# Text Summarization
def TextSummarize(Text, lang):
    translated = translator.translate(Text, dest='en')
    res = summarizer(translated.text, max_length=200, min_length=30, do_sample=False)
    if(lang == "en"):
        return res[0]['summary_text']
    else:
        pp = translator.translate(res[0]['summary_text'], dest=lang)
        return pp.text

@app.route("/")
def first():
    return page1()

@app.route("/home")
def page1():
    return render_template('home.html')

@app.route("/linkemb")
def page2():
    return render_template('linkemb.html')

@app.route("/filemb")
def page3():
    return render_template('filemb.html')

@app.route('/home', methods=['POST'])
def getText():
    userInput = request.get_json(force=True)
    return TextSummarize(userInput['text'], userInput['lang'])

@app.route('/linkemb', methods=['POST'])
def getLink():
    userInput = request.get_json(force=True)
    return LinkSummarize(userInput['text'], userInput['lang'])

@app.route('/filemb', methods=['POST'])
def getFile():
    userInput = request.get_json(force=True)
    return FileSummarize(userInput['link'], userInput['lang'], userInput['ext'])

if __name__ == "__main__":
    app.run(debug = True)
