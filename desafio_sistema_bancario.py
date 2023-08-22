#Sistema bancário:
usuario = input("informe seu nome:")
saldo = 0
extrato = ""
saque_diario = 0
operacao = 0

while operacao != 4:
    operacao = int(input(f"""
    ====================================
    Saldo: R$ {saldo}
    ====================================
    Olá, {usuario}
    Digite o número correspondente à operação desejada:
    [1] - Depósito.
    [2] - Saque.
    [3] - Extrato
    [4] - Sair.
    ====================================
    """))

    if operacao == 1: 
        valor_deposito = float(input("Qual valor você deseja depositar?\n"))
        if valor_deposito < 0: 
            print("Não é possível efetuar um depósito com esse valor")
        else:
            print(f'Você efetuou um depósito no valor de R${valor_deposito}')
            saldo = saldo + valor_deposito
            extrato += f'#Depósito: R${valor_deposito} \n'
    elif operacao == 2:
        if saque_diario >= 3:
                print("Você atingiu o limite de saque diário, tente novamente daqui a 24h")
        else:
            valor_saque = float(input("Qual valor você deseja sacar?\n"))
            if valor_saque > 500:
                print("Não é possível efetuar um saque com esse valor, o limite de saque é de R$500,00 por operação")
            elif valor_saque > saldo:
                print("Não é possível efetuar o saque por falta de saldo")
            elif saque_diario <= 3: 
                print(f'Você efetuou um saque no valor de R${valor_saque}')
                saldo = saldo - valor_saque
                saque_diario = saque_diario + 1
                extrato += f'#Saque: R${valor_saque} \n'
    elif operacao == 3:
        print(f'EXTRATO BANCÁRIO:\n{extrato}')
    elif operacao == 4:
        print(f'Muito obrigado pela preferência, {usuario}. Até logo!')
    else:
        print("Operação inválida! Por favor selecione novamente a operação desejada.")