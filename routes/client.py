from flask import Blueprint, render_template, request
from database.models.cliente import Cliente

client_route= Blueprint('client', __name__)
    
@client_route.route('/')
def lista_client():
    clientes =Cliente.select()
    return render_template('listaclientes.html', clientes=clientes)
    
@client_route.route('/', methods=['POST'])
def inserir_client():
    "inserir cliente no db"
    data= request.json
    print(data)
    novo_usuario= Cliente.create(
        name= data['Nome'],
        email= data['Email']
    )
    return render_template('item_cliente.html', cliente= novo_usuario)

@client_route.route('/new')
def for_new_client():
    return render_template('form_client.html')

@client_route.route('/<int:client_id>' )
def detalhe_client(client_id):
    cliente= Cliente.get_by_id(client_id)
    return render_template('detalhe_cliente.html', cliente= cliente)

@client_route.route('/<int:client_id>/edit')
def form_edit_client(client_id):
    cliente= Cliente.get_by_id(client_id)
    return render_template('form_client.html', cliente= cliente)

@client_route.route('/<int:client_id>/update', methods=['PUT'])
def update_client(client_id):
    data = request.json
    clienteh= Cliente.get_by_id(client_id)
    clienteh.name= data['Nome']
    clienteh.email= data['Email']        
    clienteh.save()
    return render_template('item_cliente.html', cliente= clienteh)        

@client_route.route('/<int:client_id>/delete', methods=['DELETE'])
def delete_client(client_id):
    cliente= Cliente.get_by_id(client_id)
    cliente.delete_instance()


