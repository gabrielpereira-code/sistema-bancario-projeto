menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito:\tR$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: R$ "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite de R$ 500,00.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diários excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")

        if not extrato:
            print("Não foram realizadas movimentações.")

        else:
            print(extrato)

        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=========================================")

    elif opcao == "q":
        print("Obrigado por utilizar nosso sistema bancário!")
        break

    else:
        print("Operação inválida, selecione novamente a operação desejada.")