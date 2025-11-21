'''
Arquivo de uso da classe myCrud.
para realizar operações de criar, ler, inserir, alterar e excluir.
Serve apenas para demonstrar e operar a classe CRUD.
'''


from mycrud import myCrud

#Instanciando a Classe
crud = myCrud()

# Criar tabelas
dados = {
    'tabela': 'fornecedores',
    'campos': {
        'nome': 'TEXT',
        'cnpj': 'TEXT'
    }
}
crud.createTable(dados)

# Ler
dados = {
    'tabela': 'fornecedores',
    'campos': {
        'todos': '*',
    }
}
crud.readTable(dados)

#Inserir
dados = {
'tabela': 'fornecedores',
'campos': {
    'nome': 'UGB',
    'cnpj': '72.741.815/0001-32'
    }
}
crud.insertOnTable(dados)

#Alterar
dados = {
    'tabela': 'fornecedores',
    'campos': {
        'nome': 'UGB',
        'cnpj': '72.741.815/0001-32'
    },
    'id': 1
}
crud.changeOnTable(dados)

# Deletar
dados = {
    'tabela': 'fornecedores',
    'id': 1
}
crud.deleteOnTable(dados)

# Fechar Conexão
crud.closeConnect()