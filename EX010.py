#Exercício Conversor de Moedas

r = float(input('Quanto de dinheiro você tem na sua carteira? R$'))
d = r / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(r, d))
