from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def FrotasdeCarros():
    # Define as variáveis que serão enviadas para o template
    variaveis = {
        'titulo': 'FrotasdeCarros',
        'mensagem': 'tela de login.'
    }
    # Renderiza o template 'login.html' passando as variáveis
    return render_template('', **variaveis)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def Telademenu():
    render_template('Tela-de-cadastrar-veículo.html')