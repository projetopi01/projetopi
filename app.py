from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Credenciais de usuário (apenas para demonstração, não use hardcoded em um ambiente de produção)
USUARIO = 'usuario'
SENHA = 'senha'

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/submit_login', methods=['POST'])
def submit_login():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    if usuario == USUARIO and senha == SENHA:
        # Se as credenciais estiverem corretas, redirecione para a página principal
        return redirect(url_for('index'))
    else:
        # Se as credenciais estiverem incorretas, redirecione de volta para a página de login
        return redirect(url_for('login'))

@app.route('/submit', methods=['POST'])
def submit():
    nome = request.form.get('nome')
    if nome:
        return render_template('success.html', nome=nome)
    else:
        return render_template('success.html')

@app.route('/submit_all', methods=['POST'])
def submit_all():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
