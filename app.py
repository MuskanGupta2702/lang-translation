from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        source_lan = request.form['src']
        translated_to = request.form['to']
        inputchr = str(request.form['text'])
        translated_text = translator.translate(inputchr, src=source_lan, dest = translated_to)
        d = {}
        d['output'] = translated_text.text
        print(f"The Translated Text is: {translated_text.text}")
        return d
    
if __name__ == '__main__':
    app.run(debug=True)