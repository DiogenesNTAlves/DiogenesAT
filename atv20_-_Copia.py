n1 = float(input('Digite a sua nota:'))
n2 = float(input('Digite a sua nota:'))
n3 = float(input('Digite a sua nota:'))
total = (n1+n2+n3)//3
if (total==10):
    print('Aprovado com Distinção')
elif (total>=7):
    print('Aprovado')
else:
    print('Reprovado')