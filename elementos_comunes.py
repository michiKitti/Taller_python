"""
Este programa compara dos listas de elementos numéricos y
muestra cuáles elementos están en ambas, cuáles están solo
en la primera y cuáles solo en la segunda.
"""

def comparar_listas(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)

    en_ambas = set1 & set2
    solo_en_primera = set1 - set2
    solo_en_segunda = set2 - set1

    return (en_ambas, solo_en_primera, solo_en_segunda)

# Ejemplo de uso
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

resultado = comparar_listas(lista1, lista2)

print("Elementos en ambas listas:", resultado[0])
print("Solo en la primera lista:", resultado[1])
print("Solo en la segunda lista:", resultado[2])
