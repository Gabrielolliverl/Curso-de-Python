"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
# numero =  input('Digite algum numero inteiro ')

# if numero.isdigit():
    
#     numero_int =  int(numero)
#     numero_par = numero_int % 2 == 0
#     numero_impar = numero_int % 1 == 0
    
#     if numero_par:
#         print(f'Número {numero_int} é par ')
#     else:
#         print(f'Número {numero_int} é impar ')
    

# else:
#     print('Não é um numero inteiro ')




"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


horas = input('Que horas são ?')


if horas.isdigit():
    
    horas_int = int(horas)
        
    if horas_int >= 0  and  horas_int  <= 11:
        print('Bom dia meu polvo')
    elif   horas_int >= 12  and  horas_int  <= 17:
        print("Boa tarde")
    elif   horas_int >= 18  and  horas_int  <= 23:
        print("Boa Noite")     

else:
    print(' Não indentifiquei')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""