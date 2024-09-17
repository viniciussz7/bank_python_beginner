def depositar(valor, saldo):
    saldo += valor
    return saldo
        
def sacar(valor, saldo):
    saldo -= valor
    return saldo    

menu = """
    [d] = depositar
    [s] = sacar
    [e] = extrato
    [q] = sair
    
    => """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float (input("Informe o valor do deposito: "))
        
        if valor > 0:
            saldo = depositar(valor, saldo)
            print("Deposito realizado!")
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Operacao falhou! O valor informado eh invalido.")
        
    elif opcao == "s":
        valor = float (input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques > LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operacao falhou! Voce nao tem saldo suficiente.")
        elif excedeu_limite:
            print("Operacao falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operacao falhou! Voce excedeu o limite diario de saques.")
        elif valor > 0:
            saldo = sacar(valor, saldo)
            print("Saque realizado!")
            extrato += f"Saque: R$ {valor:.2f}\n"
        else:
            print("Operacao falhou! O valor informado eh invalido.")
        
        numero_saques += 1
            
    elif opcao == "e":
        print("========= Extrato =========")
        print("\nNao foram realizadas movimentacoes." if not extrato else extrato)              
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================")
        
    elif opcao == "q":
        break
    
    else:
        print("Operacao invalida, por favor selecione novamente a operação desejada.")