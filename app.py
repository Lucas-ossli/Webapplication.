# Ao abrir o GitPod, execute:
# pip install -r requirements.txt

from flask import Flask, render_template, request
from uuid import uuid4

app = Flask(__name__)

commits = [
    {'id': 1, 'nome': 'Fulano', 'email': 'fulano@email.com', 'telefone': '124123'},
    {'id': 2, 'nome': 'Ciclano', 'email': 'ciclano@email.com', 'telefone': '1254124'},
    {'id': 3, 'nome': 'Beltrano', 'email': 'beltrano@email.com', 'telefone': '112312'},
]

@app.route('/')
def index():
    return render_template('index.html', c=commits)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])
def save():
    nome = request.form['nome']         # <input name="nome" ...
    email = request.form['email']       # Sempre será uma string!
    telefone = request.form['telefone']
    commits.append({"id": uuid4(), "nome": nome, "email": email, "telefone": telefone})
    return render_template('index.html', c=commits)

# Trabalho Final da Disciplina:
# Implementar o delete 
# Implementar o update (rota para mostrar os dados no form e outra para salvar os dados)
# Salvar os dados, conforme forem sendo manipulados, em um arquivo CSV.

@app.route('/delete/<id>')
def delete(id):
    id = int(id)
    for i,item  in enumerate(commits):
        if item['id'] == id:
            del commits[i]
    return render_template('index.html', c=commits)








@app.route('/update/<id>')
def update(id):
    
    return render_template('update.html')


@app.route('/update2/<id>', methods=['GET'])
def update2(id):
    nome = request.form['nome']         # <input name="nome" ...
    email = request.form['email']       # Sempre será uma string!
    telefone = request.form['telefone']
    
    for i,item  in enumerate(commits):
        if item['id'] == id:
            update={'id': id , 'nome': nome, 'email': email, 'telefone':telefone}
            commits[i] = update

    return render_template('index.html', c=commits)









app.run(debug=True)





# CLIENTE -- SERVIDOR
# Navegador -- AWS (Flask)

# Client -> REQUEST (Mensagem HTTP) -> Server 
# Server -> RESPONSE (Mensagem HTTP) -> CLIENTE

# HTTP (HyperText Transfer Protocol)
# HTML (HyperText Markup Language)

# Mensagem HTTP: 
# Header
# Body
# METHOD (GET, POST), Métodos suportados pelos navegadores.
# GET -> DADOS PELA URL
# POST -> OCULTO OS DADOS (NÃO MOSTRA NA URL)

# METHOD (API = GET, POST, PUT, DELETE, PATCH, OPTIONS)

# API REST
# POST   (C)REATE
# GET    (R)EAD
# PUT    (U)PDATE
# PATCH  (U)PDATE PARCIAL
# DELETE (D)ELETE