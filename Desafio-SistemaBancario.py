""" Sistema Bancário - Implementa depósitos, saques e estratos """
SELECAO = """

(d/D) Depositar
(s/S) Sacar
(e/E) Extrato
(x/X) Sair

=> """

SAQUES_MAX = 3
MAIOR_LIMITE = 500
saldo = 0
qtd_saques = 0
saida = ""

while True:

    escolha = input(SELECAO)

    if escolha in ('D', 'd'):
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            saida += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif escolha in ('S', 's'):
        valor = float(input("Informe o valor do saque: "))

        saldo_maior = valor > saldo

        passou_limite = valor > MAIOR_LIMITE

        excesso_de_saques = qtd_saques >= SAQUES_MAX

        if saldo_maior:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif passou_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excesso_de_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            saida += f"Saque: R$ {valor:.2f}\n"
            qtd_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif escolha in ('E', 'e'):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not saida else saida)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif escolha in ('X', 'x'):
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
