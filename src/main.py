"""
Autor: Daniel Torres de Andrade
Version: 1.1.0

Sistema bancário com funcionalidades de depósito, saque, extrato, criação de conta e cliente.
"""

from classes import PessoaFisica
from classes import ContaCorrente
from classes import Saque
from classes import Deposito
import textwrap


print("\nBEM VINDO AO BANCO TORRES!") # Imprime no terminal mensagem de boas vindas.


def menu() -> str:
    """
    Função para exibir o menu principal e obter a opção do usuário.

    Returns:
        str: A opção do usuário.
    """

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
    # Use textwrap.dedent para remover indentação do menu
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf: str, clientes: list) -> PessoaFisica | None:
    """
    Função para filtrar clientes pela CPF.

    Args:
        cpf (str): CPF do cliente.
        clientes (list): Lista de clientes.

    Returns:
        cliente (classes.PessoaFisica): O cliente encontrado. Se não encontrado, None.
    """

    # Filtra os clientes pela CPF
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]

    # Retorna o primeiro cliente filtrado ou None se não encontrado
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente: PessoaFisica) -> ContaCorrente | None:
    """
    Função para recuperar a conta do cliente.

    Args:
        cliente (PessoaFisica): O cliente.

    Returns:
        classes.ContaCorrente | None: A conta do cliente. Se o cliente não possuír conta, None.
    """

    if not cliente.contas:
        print("\n=== Cliente não possui conta! ===")
        return None

    # FIXME: não permite cliente escolher a conta
    # Por enquanto, retorna a primeira conta do cliente
    return cliente.contas[0]


def depositar(clientes: list) -> None:
    """
    Função para realizar depósitos na conta do cliente.

    Ela pergunta o CPF do cliente e verifica se o cliente existe. Se não,
    imprime mensagem de erro e sai. Se sim, pega a primeira conta do cliente,
    remove o valor do depósito do saldo da conta e registra a transação no
    histórico da conta.
    """

    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n=== Cliente não encontrado! ===")
        return

    # Pergunta o valor do depósito
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    # Recupera a conta do cliente
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    # Realiza a transação e registra no histórico da conta
    cliente.realizar_transacao(conta, transacao)


def sacar(clientes: list) -> None:
    """
    Função para realizar saques na conta do cliente.

    Ela pergunta o CPF do cliente e verifica se o cliente existe. Se não,
    imprime mensagem de erro e sai. Se sim, pega a primeira conta do cliente,
    remove o valor do saque do saldo da conta e registra a transação no
    histórico da conta.

    Args:
        clientes (list): lista de clientes
    """

    #FIXME: precisa limitar o valor do saque
    #FIXME: precisa tratar o erro quando o CPF é inválido
    #FIXME: precisa tratar o erro quando o valor do saque é maior que o saldo da conta
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    # Recupera a conta do cliente
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    # Realiza a transação e registra no histórico da conta
    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes: list) -> None:
    """
    Função para exibir o extrato bancário do cliente.

    Ela pergunta o CPF do cliente e verifica se o cliente existe. Se não,
    imprime mensagem de erro e sai. Se sim, pega a primeira conta do cliente
    e imprime o extrato bancário com as transações realizadas e o saldo atual.
    """

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


def criar_cliente(clientes: list) -> None:
    """
    Função para criar um novo cliente.

    Ela pergunta o CPF do cliente e verifica se o cliente existe. Se não,
    prossegue com a inclusão dos outros dados e adiciona o cliente na lista
    de clientes.

    Args:
        clientes (list): lista de clientes
    """

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

        # Pergunta a data de nascimento do cliente
        data_nascimento_dia = input("Digite o dia de nascimento do cliente: ")
        data_nascimento_mes = input("Digite o mes de nascimento do cliente: ")
        data_nascimento_ano = input("Digite o ano de nascimento do cliente: ")
        data_nascimento_completa = f"{data_nascimento_dia}/{data_nascimento_mes}/{data_nascimento_ano}"
    
        # Pergunta o endereço do cliente
        logradouro = input("Digite o logradouro: ")
        numero = input("Digite o numero: ")
        bairro = input("Digite o bairro: ")
        cidade = input("Digite o cidade: ")
        estado_sigla = input("Digite a sigla do estado(XX): ")
        endereco_completo = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado_sigla}"

    # Cria o objeto cliente com os dados informados
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento_completa, cpf=cpf, endereco=endereco_completo)

    # Adiciona o cliente na lista de clientes
    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


def criar_conta(numero_conta: int, clientes: list, contas: list) -> None:
    """
    Função para criar uma nova conta.

    Ela pergunta o CPF do cliente e verifica se o cliente existe. Se sim,
    cria uma nova conta com o número de conta informado, adiciona a conta
    na lista de contas e na lista de contas do cliente.

    Args:
        numero_conta (int): número da conta a ser criada
        clientes (list): lista de clientes
        contas (list): lista de contas
    """

    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n=== Cliente não encontrado, fluxo de criação de conta encerrado! ===")
        return
    
    # Verifica se o cliente é uma instância de PessoaFisica
    if not isinstance(cliente, PessoaFisica):
        print("\n=== Erro: Cliente não é uma instância de PessoaFisica ===")
        return

    # Cria uma nova conta com o número de conta informado
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas: list) -> None:
    """
    Função para listar todas as contas cadastradas.

    Ela itera sobre a lista de contas e imprime as informações de cada uma
    delas. Se a conta possuir um cliente com nome, as informações da conta
    são impressas. Caso contrário, um erro é impresso.

    Args:
        contas (list): lista de contas a serem impressas
    """

    for conta in contas:
        if hasattr(conta.cliente, 'nome'):
            # A conta tem um cliente com nome, imprime as informações
            print("=" * 100)
            print(textwrap.dedent(str(conta)))
        else:
            # A conta não tem um cliente com nome, imprime um erro
            print("\n=== Erro: Conta com cliente inválido detectada ===")


def main() -> None:
    """
    Função Main do sistema bancário.

    Esta função será chamada quando o script for executado. Ela exibirá
    o menu principal e executará as funções de acordo com a escolha do usuário.

    Args:
        None

    Returns:
        None
    """
    clientes = []  # List of Client objects
    contas = []  # List of Conta objects

    while True:
        opcao = menu()  # Display the main menu

        if opcao == "1":
            depositar(clientes)  # Deposit money into an account

        elif opcao == "2":
            sacar(clientes)  # Withdraw money from an account

        elif opcao == "3":
            exibir_extrato(clientes)  # Show the account's statement

        elif opcao == "6":
            criar_cliente(clientes)  # Create a new client

        elif opcao == "4":
            # Create a new account
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "5":
            # List all accounts
            listar_contas(contas)

        elif opcao == "0":
            break  # Exit the program

        else:
            print("\n=== Operação inválida, por favor selecione novamente a operação desejada. ===")


if __name__ == "__main__":
    main()
