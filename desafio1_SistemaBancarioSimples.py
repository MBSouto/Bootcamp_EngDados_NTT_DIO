
from datetime import datetime

menu = '''
    [1] Depositar
    [2] Sacar
    [3] Extrato

    [0] Sair
'''

timelog = datetime.now().isoformat()
saldo = 0 
limite = 500
extrato = []
num_saques = 0
lim_saques = 3



while True:
    opcao = input(menu)

    if opcao == "1": # Seleciona a opção depósito
        deposito = int(input('Insira um valor para depósito: '))
        if deposito > 0: # Verifica se o valor de depósito é positivo
            saldo += deposito # Adiciona o valor ao saldo
            extrato.append(f"{timelog} - Depósito: R$ {deposito:.2f}") # Adiciona a transação ao extrato
            print('Depósito realizado com sucesso!')
        else:
            print('Valor inválido. Tente novamente!')       
    
    elif opcao == "2":# Seleciona a opção saque
        saque = int(input('Informe o valor que deseja sacar: '))
        if saque > 0: # Verifica se o valor de depósito é positivo
            if num_saques < lim_saques: # Verifica o limite de 3 saques diários     
                if saldo > saque: # Verifica se há saldo para a transação 
                    if saque <= limite: # Verifica se a transação excede o valor máximo por saque 
                        saldo -= saque # Subtrai do saldo o valor da transação
                        extrato.append(f"{timelog} - Saque: R$ {saque:.2f}") # Adiciona a transação ao extrato
                        num_saques += 1 # Adiciona 1 numero de saque realizado
                        print(f'Saque no valor de R$ {saque:.2f} realizado com sucesso!')
                    else:
                        print('Não foi possível realizar esta operação, você excedeu o valor máximo de saque! \nInsira um valor menor que R$500.00')
                else:
                    print('Não foi possível realizar esta operação, seu saldo é insulficiente!')
            else:
                print('Não foi possível realizar esta operação, você excedeu o número de saques diários!')
        else:
                print('Valor inválido. Tente novamente!')        

    elif opcao == "3": # Seleciona a opção extrato
        print("==================== EXTRATO ====================\n")
        print(f"Não foram realizadas movimentações!" if not extrato else '\n'.join(extrato)) # Mensagem caso não haja movimentações registradas
        print(f"\nSeu saldo atual é: R$ {saldo:.2f}") # Mensagem para informar o saldo atual
        print("=================================================\n")

    elif opcao == "0": # Seleciona a opção sair
        break

    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')



## REQUISITOS DE NEGOCIO ##

# DEPÓSITO 
# Apenas valores positivos;
# Apenas 1 usuario;
# Armazenar na variável;
# Exibir no Extrato

# SAQUE
# 3 saques diários;
# limite máximo de R$500,00 por saque;
# Exibir mensagem caso haja falta de saldo; (não foi possível realizaer o saque)
# Exibir mensagem de limite de saques exedido;
# Armazenar em variável;
# Exibir no Extrato;

# EXTRATO
# Listar todos os valores de depósitos e saques realizados;
# Exibir ao final o saldo da conta;
# Valores devem estar no formato "R$ 000.00"
# Armazenar em uma variável