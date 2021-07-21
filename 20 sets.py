# add (adiciona), update (atualiza), clear, discard, union | (une), intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (elementos que estao nos dois sets, mas nao em ambos)
s1 = {1,2,3,4,5,6,7}
s1.add(1)
s1.add(1)
s1.add(1)
s1.discard(2)

print(s1)