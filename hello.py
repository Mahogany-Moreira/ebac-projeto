# Calculadora simples em Python

# Definindo nome da calculadora
print("\n******************* CALCULANDO COM MAHOGANY *******************")

# Criando operações

def soma(x,y):
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    return x / y

# Instrução inicial para o usuário
print("\nSelecione o número da operação desejada: \n")
print("\n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão\n")


# Pedindo ao usuário para inserir opção de operação desejada
opção = (input('\nDigite sua opção (1/2/3/4): '))
op1 = int(input('\nDigite o primeiro número: '))
op2 = int(input('\nDigite o segundo número: '))
    
    # Condições da operação
if opção == '1':
    print('\n')
    print(op1, '+', op2, '=', soma(op1,op2))
    print('\n')
elif opção == '2':
    print('\n')
    print(op1, '-', op2, '=', sub(op1,op2))
    print('\n')
elif opção == '3':
    print('\n')
    print(op1, '*', op2, '=', mul(op1,op2))
    print('\n')
elif opção == '4':
    print('\n')
    print(op1, '/', op2, '=', div(op1,op2))
    print('\n')
    
else:
    print('\n Operação Inválida')