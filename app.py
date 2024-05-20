from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


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

def create_tables():
    
    with app.app_context():
        db.create_all()

@app.route('/')
def index():
    return render_template('login_page.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':

        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'usuario' and password == '123456':
            
            return redirect(url_for('cadastro_gestante'))
        else:
          
            return redirect(url_for('login'))
    else:
      
        return render_template('login_page.html')

@app.route('/cadastro_gestante', methods=['GET'])
def cadastro_gestante():
    
    return render_template('cadastro_gestante.html')

@app.route('/submit_login', methods=['POST'])
def submit_login():
    
    username = request.form.get('username')
    password = request.form.get('password')

    if username == '123456' and password == '123456':
        
        return redirect(url_for('cadastro_gestante'))
    else:
       
        return redirect(url_for('login'))

@app.route('/submit', methods=['POST'])
def submit():
   
    cpf = request.form.get('cpf')
    nome = request.form.get('nome')
    data_nascimento = datetime.strptime(request.form.get('data_nascimento'), '%Y-%m-%d')
    idade = request.form.get('idade')
    nome_mae = request.form.get('nome_mae')
    data_prevista_parto = datetime.strptime(request.form.get('data_prevista_parto'), '%Y-%m-%d')
    ultima_menstruacao = datetime.strptime(request.form.get('ultima_menstruacao'), '%Y-%m-%d')
    endereco = request.form.get('endereco')
    cep = request.form.get('cep')
    cidade = request.form.get('cidade')
    estado = request.form.get('estado')
    telefone = request.form.get('telefone')

    
    novo_usuario = Usuario(cpf=cpf, nome=nome, data_nascimento=data_nascimento, idade=idade,
                           nome_mae=nome_mae, data_prevista_parto=data_prevista_parto,
                           ultima_menstruacao=ultima_menstruacao, endereco=endereco,
                           cep=cep, cidade=cidade, estado=estado, telefone=telefone)
    
   
    db.session.add(novo_usuario)
    db.session.commit()

    return render_template('success_page.html', nome=nome)

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
