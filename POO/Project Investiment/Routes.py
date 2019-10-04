from flask import Flask, render_template
from classes import Carteira_investimentos, Investimento


app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template("pg_inicial.html")

@app.route('/investimento')
def investimento():
    return render_template("pg_investimentos.html")

@app.route('/carteira-investimento')
def carteira_investimentos():
    return render_template("pg_inicial.html")

app.run()