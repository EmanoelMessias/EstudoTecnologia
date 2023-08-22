from flask import Flask, request, jsonify

app = Flask(__name__)

# Banco de dados temporário para armazenar os usuários
users = []

class User:
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

# Rota para adicionar um novo usuário via POST
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    cpf = data.get('cpf')
    nome = data.get('nome')
    data_nascimento = data.get('data_nascimento')

    if cpf is None or nome is None or data_nascimento is None:
        return jsonify({'error': 'Parâmetros incompletos'}), 400

    new_user = User(cpf, nome, data_nascimento)
    users.append(new_user)
    return jsonify({'message': 'Usuário adicionado com sucesso'}), 201

# Rota para obter dados de um usuário via GET
@app.route('/get_user/<int:cpf>', methods=['GET'])
def get_user(cpf):
    for user in users:
        if user.cpf == cpf:
            return jsonify({'cpf': user.cpf, 'nome': user.nome, 'data_nascimento': user.data_nascimento})
    
    return jsonify({'error': 'Usuário não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
