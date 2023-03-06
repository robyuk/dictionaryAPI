from flask import Flask, render_template
import pandas as pd

df = pd.read_csv('dictionary.csv')

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/v1/<word>')
def about(word):
    definition = df.loc[df['word'] == word]['definition'].squeeze()
    if isinstance(definition, str):
        status = 'OK'
    else:
        definition = word
        status = 'Word not found. Ensure the word is lowercase, except for proper nouns which should be capitalised'

    return {'word': word,
            'definition': definition,
            'status': status}


if __name__ == '__main__':
    app.run(debug=False, port=5002)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
