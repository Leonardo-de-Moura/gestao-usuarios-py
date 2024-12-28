from flask import Blueprint, render_template, request
from database.cliente import CLIENTES
from database.models.cliente import Cliente

client_route= Blueprint('client', __name__)
    
@client_route.route('/')
def lista_client():
    clientes =Cliente.select()
    return render_template('listaclientes.html', clientes=clientes)
    
@client_route.route('/', methods=['POST'])
def inserir_client():
    "inserir cliente no db"
    return render_template('item_cliente.html', cliente= novo_usuario)

@client_route.route('/new')
def for_new_client():
    return render_template('form_client.html')

@client_route.route('/<int:client_id>' )
def detalhe_client(client_id):
    cliente= list(filter(lambda c: c['id'] == client_id, CLIENTES))[0]
    return render_template('detalhe_cliente.html', cliente= cliente)

@client_route.route('/<int:client_id>/edit')
def form_edit_client(client_id):
    cliente= None
    for c in CLIENTES:
        if c["id"]==client_id:
            cliente=c
    return render_template('form_client.html', cliente= cliente)

@client_route.route('/<int:client_id>/update', methods=['PUT'])
def update_client(client_id):
    clienteh= None
    data = request.json
    for c in CLIENTES:
        if c['id'] == client_id:
            c['nome']=data['Nome']
            c['email']=data['Email']
            clienteh=c
            
    return render_template('item_cliente.html', cliente= clienteh)        

@client_route.route('/<int:client_id>/delete', methods=['DELETE'])
def delete_client(client_id):
    global CLIENTES
    CLIENTES = [ c for c in CLIENTES if c["id"] !=client_id  ]
    return {"retorno":"true"}

