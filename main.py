from flask import Flask, render_template
app = Flask(__name__)

#rota para página inicial (login)
@app.route('/')
def login():
    return render_template('login.html')

#rota para o menu principal
@app.route('/menu')
def menu():
    return render_template('menu.html')

#rota para cadastro de veículos

@app.route('/cadastrar-veiculos')
def cadastrar_veículos():
    return render_template('Tela-de-cadastrar-veículo.html')

#rotas para manutenção
@app.route('/manutenção')
def manutenção():
    return render_template('manutenção.html')

#rota para cadastro de usuários
@app.route('/cadastrar-usuario')
def cadastrar_usuario():
    return render_template('usuario/create.html')

if __name__=='__main__':
    app.run(debug=True)