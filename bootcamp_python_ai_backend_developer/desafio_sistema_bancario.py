menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = str(input(menu))

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"MOVIMENTAÇÃO BANCÁRIA - Depósito: R${valor:.2f}\n"
        else:
            print("Falha! O valor informado é inválido. Digite apenas valores positivos")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        if valor > saldo:
            print("Falha! Seu saldo é insuficiente.")

        elif valor > limite:
            print("Falha! O valor ultrapassa o limite, você só pode sacar R$500,00 por operação.")

        elif numero_saques >= LIMITE_SAQUES:
            print("Falha! Número máximo de saques excedido. Você pode sacar apenas 3 vezes por dia!")

        elif valor > 0:
            saldo -= valor
            extrato += f"MOVIMENTAÇÃO BANCÁRIA - Saque: R${valor:.2f}\n"
            numero_saques += 1

        else:
            print("Falha! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        if not extrato:
            print("Não há movimentações bancarias.")
        else:
            print(extrato)
        print(f"\nSaldo Bancário: R${saldo:.2f}")
        print("=========================================")

    elif opcao == "4":
        break

    else:
        print("Falha! Por favor, selecione apenas as operações disponiveis.")
