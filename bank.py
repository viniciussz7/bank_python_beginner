#import textwrap

def menu():
    menu = """\n
    =============== MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuario
    [q]\tSair
    
    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor>0:
        saldo += valor
        extrato += f"Deposito:\t\tR$ {valor:.2f}\n"
        print("\n=== Deposito realizado! ===")
    else:
        print("\n@@@ Operacao falhou! O valor informado eh invalido. @@@")

    return saldo, extrato
        
def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > LIMITE_SAQUES
        
    if excedeu_saldo:
        print("\n@@@ Operacao falhou! Voce nao tem saldo suficiente. @@@")
    elif excedeu_limite:
        print("\n@@@ Operacao falhou! O valor do saque excede o limite. @@@")
    elif excedeu_saques:
        print("\n@@@ Operacao falhou! Voce excedeu o limite diario de saques.@@@")

    elif valor > 0:
        saldo -= valor        
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado! ===")
    else:
        print("\n@@@ Operacao falhou! O valor informado eh invalido. @@@")
    
    return saldo, extrato    

def exibir_extrato(saldo, /, *, extrato):
    print("========= Extrato =========")
    print("\nNao foram realizadas movimentacoes." if not extrato else extrato)              
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("===========================")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Ja existe usuario com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd--mm--aaaa): ")
    endereco = input("Informe o endereco (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n=== Usuario criado! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n=== Conta criada! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuario nao encontrado, fluxo de criacao de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """

        print("=" * 50)
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
        
        if opcao == "d":
            valor = float (input("Informe o valor do deposito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == "s":
            valor = float (input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
            
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "c":
            listar_contas(contas)

        elif opcao == "q":
            break
        
        else:
            print("\n@@@ Operacao invalida, por favor selecione novamente a operação desejada. @@@")

main()