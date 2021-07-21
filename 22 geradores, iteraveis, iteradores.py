import sys

# lista = list(range(10))
#
# print(sys.getsizeof(lista))

#lista normal
l1 = [x for x in range(1000)]
print(type(l1))
#lista gerador
l2 = (x for x in range(1000))
print(type(l2))

print(sys.getsizeof(l1))
print(sys.getsizeof(l2)) #gerador bem menor na memoria
