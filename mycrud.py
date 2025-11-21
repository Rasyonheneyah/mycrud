'''
Classe para CRUD em SQLite.

Classe genérica de CRUD para SQLite, desenvolvida de forma generalista para atender empresas que precisem manipular qualquer tabela ou conjunto de dados definido dinamicamente. Suporta criação, leitura, atualização e remoção de registros, permitindo flexibilidade para trabalhar com tabelas como PRODUTOS e FORNECEDORES sem alterar a implementação.

OBS:
- [:-2] remove vírgula extra no final de colunas/placeholders.
- Prints ajudam a conferir SQL e indicar ações realizadas.
- Fechar conexão no final do uso.py é obrigatório.
- Objetivo: checar estrutura e execução do SQL; manipulação dos dados ocorre no uso.py.
'''

class myCrud:
    def __init__(self):
        import sqlite3


        self.conexao = sqlite3.connect('cliente.sqlite')
        self.cursor = self.conexao.cursor()

        print('--- CLASSE INSTANCIADA ---')

    def createTable(self, dados):
        sql = f'CREATE TABLE IF NOT EXISTS {dados['tabela']}(\n'
        sql += 'id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, '
        for campo in dados['campos']:
            sql += f'\n{campo} {dados['campos'][campo]} , '
        sql = sql[:-2] + f'\n)'
#        print(f'''{sql}''')
        self.cursor.execute(sql)
        self.conexao.commit()
        print('--- TABELA CRIADA (SE NÃO EXISTE AINDA) ---')

    def readTable(self, dados):
        sql1 = f'SELECT'
        for campo in dados['campos']:
            sql1 += f' {dados['campos'][campo]} , '
        sql2 = f' FROM {dados['tabela']};'
        sql = sql1[:-2] + sql2
#        print(f'{sql}')
        self.cursor.execute(sql)
        read = self.cursor.fetchall()
        print(f'{read}')

        print('--- TABELA VISUALIZADA ---')

    def insertOnTable(self, dados):
        sql2 = ''
        sql3= ''
        valList = []
        for campo in dados['campos']:
            sql2 += f'{campo} , '
            sql3 += f'?, '
            valList.append(dados['campos'][campo])
        sql = f'''
        INSERT INTO {dados['tabela']} ({sql2[:-2]})
        VALUES({sql3[:-2]})
        '''
#        print(f'{sql}')
        self.cursor.execute(sql, valList)
        self.conexao.commit()

        print('--- REGISTRO ADICIONADO---')

    def changeOnTable(self, dados):
        sql = f'UPDATE {dados['tabela']} \n SET'
        valList = []
        for campo in dados['campos']:
            sql += f' {campo} = ?, '
            valList.append(dados['campos'][campo])
        sql = sql[:-2] + f' \n WHERE id = ?'
        valList.append(dados['id'])
#        print(f'{sql}')
        self.cursor.execute(sql, valList)
        self.conexao.commit()
        print('--- TABELA ATUALIZADA ---')

    def deleteOnTable(self, dados):
        sql = f'DELETE FROM {dados['tabela']} \n WHERE  id = ?;'
#        print(f'{sql}')
        id = [dados['id']]
        self.cursor.execute(sql, id)
        print('--- ELEMENTO EXCLUIDO ---')

    def closeConnect(self):
        self.conexao.close()
        print('--- CONEXÃO ENCERRADA ---')

