menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
"""

saldo = 0
limite = 500
extrato = ""
n_saques = 0
L_SAQUES = 3

while True:
    opcao = input(menu)
    if opcao == "1":
        valor = float(input("Informe o valor do depósito:"))
        if valor > 0:
            saldo += valor
            extrato += "Depósito: R$", valor
        else:
            print("O valor informado é inválido.")
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        exc_saldo = valor > saldo

        exc_limite = valor > limite

        ex_saques = numero_saques >= LIMITE_SAQUES

        if exc_saldo:
            print("Você não tem saldo suficiente.")

        elif exc_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif exc_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$", valor
            n_saques += 1

        else:
            print("O valor informado é inválido.")

    elif opcao == "3":
        print("EXTRATO")
        print("Não foram realizadas movimentações.", extrato)
        print("Saldo: R$", saldo)

    elif opcao == "4":
        break

    else:
        print("Operação inválida")