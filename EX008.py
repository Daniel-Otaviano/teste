#Exercício para converter em medidas.
m = float(input('Digite o valor em metros: '))
mm = m * 1000
cm = m * 100
dm = m * 10
dam = m / 10
hm = m / 100
km = m / 1000
print('A medida de {}m, corresponde a: '.format(m))
print('{0:.0f}mm. \n{1:.0f}cm. \n{2:.0f}dm.'.format(mm, cm, dm))
print('{0}dam. \n{1}hm. \n{2}km'.format(dam, hm, km))





