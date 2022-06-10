# Ao abrir o GitPod, execute:
# pip install -r requirements.txt

from flask import Flask, render_template, request , redirect
from uuid import uuid4
import csv
app = Flask(__name__)




atores = []

with open('Filmes.csv','rt') as file_in:
    leitor = csv.DictReader(file_in)
    for i in leitor:
        atores.append(dict(i))


def saveDict():
    with open('Filmes.csv', 'wt') as file_out:
        escritor = csv.DictWriter(file_out, ['id', 'nome' , 'personagem', 'filme'])
        escritor.writeheader()
        escritor.writerows(atores)


@app.route('/')
def index():
    saveDict()
    return render_template('index.html', c=atores)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])
def save():
    nome = request.form['nome']         # <input name="nome" ...
    personagem = request.form['personagem']       # Sempre será uma string!
    filme = request.form['filme']
    atores.append({"id": str(uuid4()), "nome": nome, "personagem": personagem, "filme": filme})
    return redirect('/')

# Trabalho Final da Disciplina:
# Implementar o delete 
# Implementar o update (rota para mostrar os dados no form e outra para salvar os dados)
# Salvar os dados, conforme forem sendo manipulados, em um arquivo CSV.

@app.route('/delete/<id>')
def delete(id):
    for i,item  in enumerate(atores):
        if item['id'] == id:
            del atores[i]
    return redirect('/')






@app.route('/update/<id>')
def update(id):
    ator=[]
    for i,item  in enumerate(atores):
        if item['id'] == id:
            ator = item
           
    return render_template('update.html', c = ator )



@app.route('/update2/', methods=['POST'])
def update2():
    nome = request.form['ator']         # <input name="nome" ...
    personagem = request.form['personagem']       # Sempre será uma string!
    filme = request.form['filme']
    
    for i,item  in enumerate(atores):
        if item['id'] == c['id']:
            id = c['id']
            update={'id': id , 'nome': nome, 'personagem': personagem, 'filme':filme}
            atores[i] = update
   

    return redirect('/')









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