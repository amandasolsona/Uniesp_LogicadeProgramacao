#Desenvolva um programa para calcular a venda de maçãs em uma banca de feira. O cliente compra maçãs
# custando R $1,37 cada uma, mas caso ele compre a partir de uma dúzia pagará com desconto de 10%,
# portanto o valor da unidade ficará por R $1,24. O programa deverá receber o número de maçãs desejadas
# pelo cliente, e retornar o valor total da compra.

#Calcular a venda de maças

qtd_macas = float(input('Quantas maças você irá levar:'))

valor_maca_sem_desconto = 1.37

if qtd_macas >= 12:
    valor_total = qtd_macas * 1.24

else:
    valor_total = qtd_macas * valor_maca_sem_desconto

print(f'O você total da compra de maças é por R$ {valor_total:.2f}')
