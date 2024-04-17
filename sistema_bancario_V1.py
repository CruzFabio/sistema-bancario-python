menu = """
\n|============ Menu ============|

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair

|==============================|
\n Selecione uma opção: > """


saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("\nQual o valor do depósito: R$ "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\nDepósito realizado com sucesso!")
            print(f"Saldo disponível: R$ {saldo:.2f}")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 2:
        valor = float(input("\nQual valor deseja sacar R$ "))

        excedeu_limite = valor > limite
        excedeu_saldo = valor > saldo
        excedeu_saque = numero_de_saques >= LIMITE_SAQUE

        if excedeu_limite:
            print("Operação falhou! Valor informado excede o limite.")
        elif excedeu_saldo:
            print("Saldo insuficiente para esta operação.")
        elif excedeu_saque:
            print("Limite diário de saques atingido.")
        elif valor > 0:
            saldo -= valor
            numero_de_saques += 1
            extrato += f"Saque: R$ {valor:.2f}\n"
            print("\nSaque realizado com sucesso!")
            print(f"Saldo disponível: R$ {saldo:.2f}")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 3:
        print("\n|============ EXTRATO ============|")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n>> Saldo disponível: R$ {saldo:.2f}")
        print("|===================================|")

    elif opcao == 0:
        break
    else:
        print("Opçâo Inválida, por favor selecione uma opção válida.")