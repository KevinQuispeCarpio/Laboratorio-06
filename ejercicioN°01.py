# 17.1 Realizar operaciones de unión, intersección y diferencia de conjuntos
conjunto1 = {1, 2, 3, 4, 5}  # Creamos el conjunto 1°
conjunto2 = {2, 8, 9, 11, 21}  # Creamos el conjunto 2°
conjunto3 = {2, 8, 69, 45, 32}

print('A = ', conjunto1)
print('B = ', conjunto2)
print('C = ', conjunto3)
# Unimos los dos conjuntos gracias a "|", que nos ayuda a realizar la union
print('A U B U C = ', (conjunto1 | conjunto2|conjunto3))
# Hallamos la intersección de conjuntos usando "&", que nos sirve para intersectar
print('A ∩ B ∩ C = ', (conjunto1 & conjunto2 & conjunto3))
# Acá encontramos la diferencia de conjuntos usando "-", que sirve para ello
print('A - B - C = ', (conjunto1 - conjunto2 - conjunto3))
