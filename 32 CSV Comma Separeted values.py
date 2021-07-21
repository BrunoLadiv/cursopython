import csv

with open('clientes.csv', 'r') as arquivo:
    dados = csv.reader(arquivo) #.dictreader importar como dicionario
#   pra cada dado em dados: print dado
    for dado in dados:
        print (dado)