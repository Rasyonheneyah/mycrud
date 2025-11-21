# CRUD em Python com SQLite

Este repositório contém uma implementação simples de um CRUD utilizando Python e SQLite.
A estrutura foi projetada para receber dados através de dicionários padronizados, mantendo o código flexível, reutilizável e fácil de integrar em outros projetos.

## 📌 Funcionalidades

* Criar tabelas automaticamente caso não existam
* Inserir registros
* Ler registros (por ID ou tabela inteira)
* Atualizar registros
* Deletar registros
* Operações usando parâmetros seguros (sem concatenação manual)

## 🗂 Estrutura dos Dicionários Aceitos

### **Criação de tabela**

```
{
    "tabela": "nomeDaTabela",
    "campos": {
        "coluna1": "TIPO",
        "coluna2": "TIPO",
        ...
    }
}
```
### **Leitura de Tabela**

#### **Ler Toda Tabela**
```
dados = {
    'tabela': 'nomeDaTabela',
    'campos': {
        'todos': '*',
    }
}
```

#### **Ler Tabela Por Coluna**
```
dados = {
    "tabela": "nomeDaTabela",
    "campos": {
        "coluna1": "coluna1",
        "coluna2": "coluna2",
        "coluna3": "coluna3"
    }
}
```

### **Inserção**

```
{
    "tabela": "nomeDaTabela",
    "campos": {
        "coluna1": valor,
        "coluna2": valor,
        ...
    }
}
```

### **Atualização**

```
{
    "tabela": "nomeDaTabela",
    "campos": {
        "coluna1": novoValor,
        "coluna2": novoValor,
        ...
    },
    "id": valorDoId
}
```

### **Exclusão**

```
{
    "tabela": "nomeDaTabela",
    "id": valorDoId
}
```

## 🔧 Como Utilizar

### **1. Instanciar a classe**

```
crud = MyCrud()
```

### **2. Chamar métodos passando o dicionário adequado**

```
crud.createTable(dict)
crud.readTable(dict)
crud.insertOnTable(dict)
crud.changeOnTable(dict)
crud.deleteOnTable(dict)
```

## 📄 Sobre o arquivo `use.py`

O arquivo `use.py` contém apenas o código de uso do CRUD.
Ele funciona como o lugar onde você monta os dicionários e chama os métodos.
Serve como "arquivo de teste" e demonstração da utilização.

## 📌 Observações importantes

* A conexão é aberta automaticamente a cada operação.
* Caso alguma conexão fique aberta sem fechar, o SQLite mantém até o processo Python encerrar (VSCode fecha ao parar a execução).
* O padrão de dicionários facilita a expansão e organização do CRUD.
