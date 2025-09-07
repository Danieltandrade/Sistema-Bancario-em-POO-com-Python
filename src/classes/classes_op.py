"""
Módulo de classes para o sistema bancário.

Contém as definições das classes Cliente, Conta, ContaCorrente, Historico, 
Transacao, Saque e Deposito.
"""

#Importação de módulos que serão utilizados no projeto
from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    """
    Classe que representa um cliente do banco.

    Atributos:
        endereco (str): Endereço do cliente.
        contas (list): Lista de contas associadas ao cliente.
    
    Métodos:
        realizar_transacao(conta, transacao): Realiza uma transação em uma conta.
        adicionar_conta(conta): Adiciona uma conta à lista de contas do cliente.
    """

    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    """
    Classe que representa uma pessoa física, herda de Cliente.

    Atributos:
        nome (str): Nome completo da pessoa fisica.
        data_nascimento (str): Data de nascimento da pessoa fisica.
        cpf (str): CPF da pessoa fisica.
        endereco (str): Endereço da pessoa fisica.

    Métodos:
        Herda os métodos da classe Cliente.
    """

    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class Conta:
    """
    Classe que representa uma conta bancária.

    Atributos:
        _saldo (float): Saldo da conta.
        _numero (str): Número da conta.
        _agencia (str): Agência da conta.
        _cliente (Cliente): Cliente associado a conta.
        _historico (Historico): Histórico de transações da conta.

    Métodos:
        sacar(valor): Realiza um saque na conta.
        depositar(valor): Realiza um depósito na conta.
        nova_conta(cls, cliente, numero): Cria uma nova conta.
    """

    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n=== Operação falhou! Você não tem saldo suficiente. ===")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n=== Operação falhou! O valor informado é inválido. ===")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n=== Operação falhou! O valor informado é inválido. ===")
            return False

        return True


class ContaCorrente(Conta):
    """
    Classe que representa uma conta corrente, herda de Conta.

    Atributos:
        _limite (float): Limite de saques da conta corrente.
        _limite_saques (int): Limite de saques da conta corrente.

    Métodos:
        sacar(valor): Realiza um saque na conta corrente.
        __str__(): Retorna uma representação em string da conta corrente.
    """

    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n=== Operação falhou! O valor do saque excede o limite. ===")

        elif excedeu_saques:
            print("\n=== Operação falhou! Número máximo de saques excedido. ===")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    """
    Classe que representa o histórico de transações de uma conta.

    Atributos:
        _transacoes (list): Lista de transações realizadas na conta.
    """

    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


class Transacao(ABC):
    """
    Classe abstrata que representa uma transação bancária.

    Métodos abstratos:
        valor: Retorna o valor da transação.
        registrar(conta): Registra a transação em uma conta.
    """

    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    """
    Classe que representa um saque, herda de Transacao.

    Atributos:
        _valor (float): Valor do saque.

    Métodos:
        valor: Retorna o valor do saque.
        registrar(conta): Registra o saque em uma conta.
    """

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    """
    Classe que representa um depósito, herda de Transacao.

    Atributos:
        _valor (float): Valor do depósito.

    Métodos:
        valor: Retorna o valor do depósito.
        registrar(conta): Registra o depósito em uma conta.
    """

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
