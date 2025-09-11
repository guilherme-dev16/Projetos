from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

pedidos_recebidos = []

@app.route('/pedido', methods=['POST'])
def receber_pedido():
    dados = request.json
    pedidos_recebidos.append(dados)
    print(f"📦 Pedido recebido de {dados['nome']} - total de {len(pedidos_recebidos)} pedidos")
    return jsonify({"mensagem": "Pedido recebido com sucesso!"})

@app.route('/pedidos', methods=['GET'])
def listar_pedidos():
    return jsonify(pedidos_recebidos)

if __name__ == '__main__':
    app.run(debug=True)
for item in any['itens']:
    print(f"  - {item['name']} x {item['quantity']} = R$ {item['price'] * item['quantity']:.2f}")
    if 'observacoes' in item and item['observacoes']:
        print(f"    Observações: {item['observacoes']}")
