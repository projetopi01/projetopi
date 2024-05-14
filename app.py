from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form.get('nome')
    if nome:
        return render_template('success.html', nome=nome)
    else:
        return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
