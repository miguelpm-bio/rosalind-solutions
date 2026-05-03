# 1. La secuencia original
dna = "AAAACCCGGT"

# 2. Invertimos la cadena (leída de atrás hacia adelante)
dna_invertido = dna[::-1]

# 3. Creamos una tabla de cambios: A->T, T->A, C->G, G->C
tabla = str.maketrans("ATCG", "TAGC")

# 4. Aplicamos los cambios y guardamos el resultado
resultado = dna_invertido.translate(tabla)

# 5. Mostramos el resultado final
print(resultado)
