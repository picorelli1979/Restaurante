from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index()->str:
    return render_template('cardapio.html')
    
@app.route('/cardapio')
def pagina_inicial()->str:
    return render_template('cardapio.html')

@app.route('/cardapio/pizza')
def pagina_pizza()-> str:
    return render_template('pizza.html')

@app.route('/cardapio/hamburguer')
def pagina_hamburguer()-> str:
    return render_template('hamburguer.html')

@app.route('/cardapio/pedido')
def pagina_pedido()-> str:
    return render_template('pedido.html')

@app.route('/cardapio/pagina_final')
def pagina_final()-> str:
    return render_template('pagina_final.html')

@app.route('/cardapio/reservas')
def pagina_reservas()-> str:
    return render_template('reservas.html')

@app.route('/cardapio/contatos')
def pagina_contatos()-> str:
    return render_template('contatos.html')

@app.route('/cardapio/localizacao')
def pagina_localização()-> str:
    return render_template('localização.html')

if __name__ == '__main__':
   app.run(debug=True)

