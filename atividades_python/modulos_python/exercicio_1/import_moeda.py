
# Testando as funções

import moeda 

print(f'Taxa de juros aplicada no parcelamento da compra foi de 40% ao mês: R$ {moeda.aumentar(300, 40):.2f}')
print(f'Taxa de desconto aplicada no pagamento à vista foi de 70% de desconto: R$ {moeda.diminuir(300, 70):.2f}')
print(f'Valor no pós blackfriday: R$ {moeda.dobro(300):.2f}')
print(f'Desconto aplicado no pagamento à vista: R$ {moeda.metade(300):.2f}')

       