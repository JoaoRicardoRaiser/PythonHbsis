from flask import Flask, render_template, request, redirect
from alunos import Alunos
pagina_nome = "Lista Alunos"
aluno1 = Alunos("João","Ricardo Raiser", 47984244178)
aluno2 = Alunos("Alessandra", "Priester", 47996077716)
aluno3 = Alunos("Sheila", "Rensi", 47984226293)
aluno4 = Alunos("João", "Paulo", 47984998889)
aluno5 = Alunos("Paulo", "Henrique de Souza", 4732340447)
lista_alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]

app = Flask(__name__)
@app.route('/')
def Inicio():    
    return render_template('index.html', nome=pagina_nome, lista = lista_alunos)

@app.route("/novo")
def novo():
    return render_template('novo.html') 

@app.route("/salvar", methods = ["POST"]) 
def salvar():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    telefone = request.form['telefone']
    novo_aluno = Alunos (nome,sobrenome,telefone)
    lista_alunos.append(novo_aluno)
    return redirect("/")
app.run()