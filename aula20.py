primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

valor_1 = int(primeiro_valor)
valor_2 = int(segundo_valor)

if valor_1 >= valor_2:
    print(f'Primeiro valor {valor_1} é maior ou igual que {valor_2}  segundo valor')
elif valor_2 >= valor_1:
    print(f'Segundo valor {valor_2} é maior ou igual que {valor_1}  segundo valor')
else:
    print('oskey')        
    