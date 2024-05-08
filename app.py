from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
   
        return render_template('success.html', nome=request.form['nome'])


@app.route('/submit_all', methods=['POST'])
def submit_all():
    if request.method == 'POST':
     
        return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
