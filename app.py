from flask import Flask, render_template, request

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para processar o formulário de cadastro e exibir a mensagem de sucesso
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Processar os dados do formulário aqui
        # Retornar a página de sucesso com render_template
        return render_template('success.html', nome=request.form['nome'])

# Rota para processar o formulário do cronograma e exibir a mensagem de sucesso
@app.route('/submit_all', methods=['POST'])
def submit_all():
    if request.method == 'POST':
        # Processar os dados do formulário aqui
        # Retornar a página de sucesso com render_template
        return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
