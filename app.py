from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        data_prevista_parto = request.form['data_prevista_parto']
        rh = request.form['rh']
        toxoplasmose = request.form['toxoplasmose']
        suab = request.form['suab']
        laqueadura = request.form['laqueadura']
        # Processar os dados aqui (por exemplo, salvar em um banco de dados)
        return render_template('success.html', nome=nome)

if __name__ == '__main__':
    app.run(debug=True)
