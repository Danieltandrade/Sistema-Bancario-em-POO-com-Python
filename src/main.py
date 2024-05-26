#Modelando Sistema Bancário com Programação Orientada a Objetos em Python
#Curso: Python Development
#Instituição: DIO.me
#Instrutor: Guilherme Arthur de Carvalho

import classes
import textwrap


print("\nBEM VINDO AO BANCO TORRES!") # Imprime no terminal mensagem de boas vindas.


def menu():
    menu = """\n
    ================ MENU ================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova Conta
    [5]\tListar Contas
    [6]\tNovo Cliente
    [0]\tSair
    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n=== Cliente não possui conta! ===")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]


def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n=== Cliente não encontrado! ===")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = classes.Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = classes.Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n=== Cliente não encontrado! ===")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


def criar_cliente(clientes):
    print("Cadastro de Clientes\n")
    
    cpf = input("Digite somente os numeros do CPF do cliente: ")

    # Verifica em cada cliente da lista se o CPF já está cadastrado.
    cliente = filtrar_cliente(cpf, clientes)
    
    if cliente:
        print("CPF digitado já está cadastrado em nosso sistema.")
        return

    # Prossegue com a inclusão dos outros dados.   
    else:
        nome = input("Digite o nome completo do cliente: ")

        data_nascimento_dia = input("Digite o dia de nascimento do cliente: ")
        data_nascimento_mes = input("Digite o mes de nascimento do cliente: ")
        data_nascimento_ano = input("Digite o ano de nascimento do cliente: ")
        data_nascimento_completa = f"{data_nascimento_dia}/{data_nascimento_mes}/{data_nascimento_ano}"
    
        logradouro = input("Digite o logradouro: ")
        numero = input("Digite o numero: ")
        bairro = input("Digite o bairro: ")
        cidade = input("Digite o cidade: ")
        estado_sigla = input("Digite a sigla do estado(XX): ")
        endereco_completo = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado_sigla}"


    cliente = classes.PessoaFisica(nome=nome, data_nascimento=data_nascimento_completa, cpf=cpf, endereco=endereco_completo)

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n=== Cliente não encontrado, fluxo de criação de conta encerrado! ===")
        return
    
    if not isinstance(cliente, classes.PessoaFisica):
        print("\n=== Erro: Cliente não é uma instância de PessoaFisica ===")
        return

    conta = classes.ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    for conta in contas:
        if hasattr(conta.cliente, 'nome'):
            print("=" * 100)
            print(textwrap.dedent(str(conta)))
        else:
            print("\n=== Erro: Conta com cliente inválido detectada ===")


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            depositar(clientes)

        elif opcao == "2":
            sacar(clientes)

        elif opcao == "3":
            exibir_extrato(clientes)

        elif opcao == "6":
            criar_cliente(clientes)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "5":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("\n=== Operação inválida, por favor selecione novamente a operação desejada. ===")


main()