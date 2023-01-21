# 17.1 Realizar operaciones de unión, intersección y diferencia de conjuntos
conjunto1 = {1, 2, 3, 4, 5}  # Creamos el conjunto 1°
conjunto2 = {2, 8, 9, 11, 21}  # Creamos el conjunto 2°

print('A = ', conjunto1)
print('B = ', conjunto2)

# Unimos los dos conjuntos gracias a "|", que nos ayuda a realizar la union
print('A U B = ', (conjunto1 | conjunto2))
# Hallamos la intersección de conjuntos usando "&", que nos sirve para intersectar
print('A ∩ B = ', (conjunto1 & conjunto2))
# Acá encontramos la diferencia de conjuntos usando "-", que sirve para ello
print('A - B = ', (conjunto1 - conjunto2))
