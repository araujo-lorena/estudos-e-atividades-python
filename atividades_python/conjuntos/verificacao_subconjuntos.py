"""Crie dois conjuntos A e B.
Verifique se A é subconjunto de B e se B é subconjunto de A.
Mostre a diferença entre os conjuntos (B - A e A - B)."""

conjunto_a ={"pizza","hanburguer","acai","lasanha","churrasco","chocolate","feijoada","salada de frutas"}
conjunto_b = {"pizza","acai","lasanha","churrasco","chocolate","feijoada","torta doce","frango caipira"}

subconjunto_a = conjunto_a.issubset(conjunto_b)
subconjunto_b = conjunto_b.issubset(conjunto_a)

diferenca_b_a = conjunto_b - conjunto_a
diferenca_a_b = conjunto_a - conjunto_b

print("A é subconjunto de B:", subconjunto_a)
print("B é subconjunto de A:", subconjunto_b)
print("Diferença B - A:", diferenca_b_a)
print("Diferença A - B:", diferenca_a_b)