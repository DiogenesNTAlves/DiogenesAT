sal = float(input('Digite o seu salario:'))
if (sal<=280.00):
    total1 = (sal*20)//100
    final1 = (total1+sal)
    print('Seu salario antes do reajuste:')
    print(sal)
    print('Percentual de aumento aplicado foi de 20%')
    print('Valor de aumento foi:')
    print(total1)
    print('Novo salario apos aumento:')
    print(final1)
elif (sal>=280.00 and sal<=700.00):
    total2 = (sal*15)//100
    final2 = (total2+sal)
    print('Seu salario antes do reajuste:')
    print(sal)
    print('Percentual de aumento aplicado foi de 15%')
    print('Valor de aumento foi:')
    print(total2)
    print('Novo salario apos aumento:')
    print(final2)
elif (sal>=700.00 and sal<=1500.00):
    total3 = (sal*10)//100
    final3 = (sal+total3)
    print('Seu salario antes do reajuste:')
    print(sal)
    print('Percentual de aumento aplicado foi de 10%')
    print('Valor de aumento foi:')
    print(total3)
    print('Novo salario apos aumento:')
    print(final3)
else:
    total4 = (sal*5)//100
    final4 = (sal+total4)
    print('Seu salario antes do reajuste:')
    print(sal)
    print('Percentual de aumento aplicado foi de 5%')
    print('Valor de aumento foi:')
    print(total4)
    print('Novo salario apos aumento:')
    print(final4)

