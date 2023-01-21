#  17.3 Calcular la diferencia simétrica entre 3 conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {0, 2, 7}
conjunto3 = {2, 8, 10, 15}
# Imprimos los 3 conjuntos
print('A = ', conjunto1)
print('B = ', conjunto2)
print('C = ', conjunto3)
# Unimos los 3 conjuntos
a = conjunto1 & conjunto2 & conjunto3
for i in a:
    conjunto1.discard(i)
    conjunto2.discard(i)
    conjunto3.discard(i)
# Hallamos la diferencia de los 3 conjuntos
print('La diferencia simétrica de los 3 conjuntos es:',
      (conjunto1 | conjunto2 | conjunto3))
