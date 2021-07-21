import json

# converter lista para arquivo jsonlist


clientes_data = {
    "1": {
        "nome": "Luiz Ot\u00e1vio",
        "sobrenome": "Miranda",
        "idade": 25,
        "altura": 1.8,
        "peso": 80.53
    },
    "2": {
        "nome": "Maria",
        "sobrenome": "Oliveira",
        "idade": 52,
        "altura": 1.67,
        "peso": 57
    },
    "3": {
        "nome": "Pedro",
        "sobrenome": "Faria",
        "idade": 32,
        "altura": 1.95,
        "peso": 113
    }
}

lista = [1,2,3,4,5,6,7,8,9]

dados_json = json.dumps(lista)


with open("clientes_data", 'r') as arquivo: #salvar variavel em arquivo json
    clientes_datapy = json.load(arquivo)


print(clientes_datapy)