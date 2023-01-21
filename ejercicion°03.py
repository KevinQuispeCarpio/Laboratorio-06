#  17.3 Calcular la diferencia simétrica entre 3 conjuntos
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {0, 2, 7}
# Imprimos los 2 conjunto
print('A = ', conjunto1)
print('B = ', conjunto2)
# Unimos los 2 conjuntos
a = conjunto1 & conjunto2 
for i in a:
    conjunto1.discard(i)
    conjunto2.discard(i)
# Hallamos la diferencia simétrica de los 2 conjuntos
print('La diferencia simétrica de los 2 conjuntos es:',(conjunto1 | conjunto2))
