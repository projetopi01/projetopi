from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de dados para o banco de dados
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), unique=True, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    idade = db.Column(db.Integer)
    nome_mae = db.Column(db.String(100), nullable=False)
    data_prevista_parto = db.Column(db.Date, nullable=False)
    ultima_menstruacao = db.Column(db.Date, nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    cep = db.Column(db.String(8), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/submit_login', methods=['POST'])
def submit_login():
    # Lógica de autenticação
    # Código omitido para brevidade
    return redirect(url_for('index'))

@app.route('/submit', methods=['POST'])
def submit():
    # Extrair os dados do formulário
    cpf = request.form.get('cpf')
    nome = request.form.get('nome')
    data_nascimento = request.form.get('data_nascimento')
    idade = request.form.get('idade')
    nome_mae = request.form.get('nome_mae')
    data_prevista_parto = request.form.get('data_prevista_parto')
    ultima_menstruacao = request.form.get('ultima_menstruacao')
    endereco = request.form.get('endereco')
    cep = request.form.get('cep')
    cidade = request.form.get('cidade')
    estado = request.form.get('estado')
    telefone = request.form.get('telefone')

    # Criar um novo objeto Usuario com os dados fornecidos
    novo_usuario = Usuario(cpf=cpf, nome=nome, data_nascimento=data_nascimento, idade=idade,
                           nome_mae=nome_mae, data_prevista_parto=data_prevista_parto,
                           ultima_menstruacao=ultima_menstruacao, endereco=endereco,
                           cep=cep, cidade=cidade, estado=estado, telefone=telefone)
    
    # Adicionar o novo usuário ao banco de dados
    db.session.add(novo_usuario)
    db.session.commit()

    return render_template('success.html', nome=nome)

if __name__ == '__main__':
    # Criar as tabelas do banco de dados se ainda não existirem
    db.create_all()
    app.run(debug=True)
