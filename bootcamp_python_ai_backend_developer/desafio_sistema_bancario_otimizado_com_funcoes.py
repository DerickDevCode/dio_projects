

def menu():
    menu = """\n
    ================ MENU ================
    [1]\nDepositar
    [2]\nSacar
    [3]\nExtrato
    [4]\nNova conta
    [5]\nListar contas
    [6]\nNovo usuário
    [7]\nSair
    => """
    return str(input(menu))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"MOVIMENTAÇÃO BANCÁRIA - Depósito: R${valor:.2f}\n"
    else:
        print("Falha! O valor informado é inválido. Digite apenas valores positivos")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Falha! Seu saldo é insuficiente.")

    elif valor > limite:
        print("Falha! O valor ultrapassa o limite, você só pode sacar R$500,00 por operação.")

    elif numero_saques >= limite_saques:
        print("Falha! Número máximo de saques excedido. Você pode sacar apenas 3 vezes por dia!")

    elif valor > 0:
        saldo -= valor
        extrato += f"MOVIMENTAÇÃO BANCÁRIA - Saque: R${valor:.2f}\n"
        numero_saques += 1
    else:
        print("Falha! O valor informado é inválido.")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não há movimentações bancarias.")
    else:
        print(extrato)
    print(f"\nSaldo Bancário: R${saldo:.2f}")
    print("=========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        return print("\n Não foi possível criar o usuário, porque já existe um usuário com esse CPF!")

    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Seu usuário foi criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n Usuário não encontrado, fluxo de criação de conta encerrado!")


def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agência:\n{conta['agencia']}
            C/C:\n{conta['numero_conta']}
            Titular:\n{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "7":
            break

        else:
            print("Opção inválida, por favor selecione novamente a operação desejada.")


main()
