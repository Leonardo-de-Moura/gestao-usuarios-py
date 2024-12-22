from flask import Blueprint, render_template, request
from database.cliente import CLIENTES

client_route= Blueprint('client', __name__)
    
"""""
rota de clientes

-/clientes/ (get)listar clientes
-/clientes/ (post) inserir clientes
-/çlientes/new (get) form para criar new client
-/clientes/id (get)- obter dados de um cliente por id
-/clientes/id/edit (get) renderizar um formulario para editar os dados
-/clientes/id/update (put) atualiza os dados
/clientes/id/delete (delete) deleta um cliente

"""
@client_route.route('/')
def lista_client():
    return render_template('listaclientes.html', clientes=CLIENTES)
    
@client_route.route('/', methods=['POST'])
def inserir_client():
    data = request.json
    print(data)
    novo_usuario = {
        "id": len(CLIENTES) +1,
        "nome": data['Nome'],
        "email": data['Email']
    }
    CLIENTES.append(novo_usuario)
    return render_template('item_cliente.html', cliente= novo_usuario)

@client_route.route('/new')
def for_new_client():
    return render_template('form_client.html')

@client_route.route('/<int:client_id>' )
def detalhe_client(client_id):
    return render_template('detalhe_client.html')

@client_route.route('/<int:client_id>/edit')
def form_edit_client(client_id):
    cliente= None
    for c in CLIENTES:
        if c["id"]==client_id:
            cliente=c
    return render_template('form_client.html', cliente= cliente)

@client_route.route('/<int:client_id>/update', methods=['PUT'])
def update_client(client_id):
    cliente= None
    data = request.json
    for c in CLIENTES:
        if c['id']== client_id:
            c['Nome']=data['Nome']
            c['Email']=data['Email']
            clienteh=c
            
    return render_template('item_cliente.html', cliente= clienteh)        

@client_route.route('/<int:client_id>/delete', methods=['DELETE'])
def delete_client(client_id):
    global CLIENTES
    CLIENTES = [ c for c in CLIENTES if c["id"] !=client_id  ]
    return {"retorno":"true"}

