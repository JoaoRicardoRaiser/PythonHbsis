from flask import Flask, render_template, request, redirect #é necessário importar a função FLASK para realizar a página.

pagina_nome = "Turma Padawans HBSIS"
cabecalhoweb = "Turma Python"

app = Flask(__name__) # Apenas sintaxe necessária para executar. Para as próximas rotas não necessita disso.
@app.route("/") # é o endereço de internet definido.
def inicio(): # é necessário um método para a rota.
    return render_template("indexweb2.html", nome=pagina_nome, cabecalho=cabecalhoweb) # return significa o que aparecerá na tela.
app.run() # Faz o app rodar.