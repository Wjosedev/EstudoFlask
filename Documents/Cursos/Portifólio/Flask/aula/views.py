from aula import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    nome = 'Willams José'
    idade = 44
    interesses = ['Python', 'flask', 'Desenvolvimento Weg']
    return render_template('index.html', nome=nome, idade=idade, interesses =interesses) 
    

@app.route('/Contato/')
def novapagina():
    return 'outra view'

