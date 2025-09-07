# Modelando-Sistema-Bancario-em-POO-com-Python


Neste projeto irei modelar o sistema bancário utlizando os conceitos de Programação Orientada a Objetos(POO).

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Python Versions](https://img.shields.io/badge/python-3.12+-blue?style=for-the-badge)](https://www.python.org/downloads/)
[![Versão do Projeto](https://img.shields.io/badge/v1.0.0-blue?style=for-the-badge&logo=github)](https://github.com/Danieltandrade/Sistema-Bancario-em-POO-com-Python/releases)
[![Build Passing](https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge)](https://github.com/Danieltandrade/Sistema-Bancario-em-POO-com-Python/actions)
[![Status: Em Desenvolvimento](https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=for-the-badge)](https://github.com/Danieltandrade/Sistema-Bancario-em-POO-com-Python)
[![Git](https://img.shields.io/badge/GIT-E44C30?style=for-the-badge&logo=git&logoColor=white)](https://git-scm.com/)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/DanielTorresAndrade)
[![Apache License 2.0](https://img.shields.io/badge/license-Apache%202.0-blue?style=for-the-badge)](https://opensource.org/licenses/Apache-2.0)

## 1. Objetivo:

O desafio consiste em modelar o sistema bancário utilizando o paradigma de __Programação Orientado a Objetos__. Para o projeto atual, as funções de deposito, saques e extrato foram modificadas para estarem ligadas a um cliente e uma conta. A conta possuí limites de saque e quantidade máxima de transações diárias conforme definições do banco:

- Valor máximo por saque: R$ 500,00
- Quantidade máxima de saques por dia: 3 saques.

## 2. Estrutura do Projeto:

Abaixo está a estrutura de pastas e arquivos do projeto:

```bash
Modelando-Sistema-Bancario-em-POO-com-Python
├── images
│   ├── UML_Desafio.png
│   ├── imagem1.png
│   └── imagem2.png
├── src
│   ├── classes
│   │   ├── __init__.py
│   │   └── classes_op.py
│   ├── __init__.py
│   └── main.py
├── .gitignore
└── README.md
```

Lembro que no meu caso utilizei o __UV__ como gerenciador de pacotes e gerenciador de projeto, mas você pode utilizar o gerenciador de pacotes de sua preferência.
Mais informações sobre podem ser vistas no link: [UV](https://docs.astral.sh/uv/)

### 2.1 Diretório images

Neste diretório estão as imagens utilizadas para demonstração do projeto em funcionamento e a imagem do modelo de classes UML.

### 2.2 Diretório src

Neste diretório estão os arquivos principais do projeto. O arquivo __"__init__.py"__ é necessário para que o Python reconheça o diretório como um pacote. O arquivo __"main.py"__ contém o código principal do projeto, onde são chamadas as funções e classes criadas.

Opções de seleção de menu do sistema bancário:

```
[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo Cliente
[5] Nova Conta
[6] Listar Contas
[0] Sair
```

### 2.3 Diretório classes

Neste diretório estão os arquivos de classes criadas para o projeto. O arquivo __"__init__.py"__ é necessário para que o Python reconheça o diretório como um pacote. O arquivo __"classes_op.py"__ contém todas as classes criadas para o projeto.

### 2.4 Arquivos .gitignore e README.md

O arquivo __".gitignore"__ é utilizado para ignorar arquivos e diretórios que não devem ser versionados pelo Git. O arquivo __"README.md"__ é este arquivo que você está lendo, onde estão as informações do projeto.

## 3. Instalação:

Para instalar o projeto, basta seguir os passos abaixo:

1. Abra o terminal ou o prompt de comando do seu sistema operacional.
2. Navegue ate o diretório do projeto.
3. Clone o repositório do projeto utilizando o comando:
   ```bash
   git clone https://github.com/Danieltandrade/Sistema-Bancario-em-POO-com-Python.git
   ```
4. Navegue ate o diretório do projeto.
5. Instale as dependências do projeto utilizando o comando:
   ```bash
   uv install
   ```
6. Após a instalação das dependências, você pode executar o projeto utilizando o comando:
   ```bash
   uv run src/main.py
   ```

## 4. Funcionalidades do Projeto:

O sistema bancário possui as seguintes funcionalidades:

- Depositar: Permite ao cliente depositar um valor em sua conta.
- Sacar: Permite ao cliente sacar um valor da sua conta.
- Extrato: Exibe o extrato bancário da conta do cliente.
- Novo Cliente: Permite ao administrador cadastrar um novo cliente.
- Nova Conta: Permite ao administrador cadastrar uma nova conta para o cliente.
- Listar Contas: Permite ao administrador listar todas as contas cadastradas.

Todas as funcionalidades foram implementadas utilizando os conceitos de Programação Orientada a Objetos, como classes, objetos, herança, polimorfismo e encapsulamento. Um modelo de classes UML foi utilizado para auxiliar na criação das classes e suas relações. Na descrição dos arquivos abaixo, estão detalhadas as funcionalidades implementadas em cada arquivo.

### 4.1 Arquivo classes.py

- Este arquivo é um módulo, onde estão as classes que serão usadas no arquivo principal __main.py__.

- Para o desafio o instrutor nos passou uma imagem com o modelo de classes __UML__ do projeto. Este modelo pode ser visto na imagem abaixo:

<img src="images/UML_Desafio.png">


- Os módulos __abc__ e __datetime__ foram importados no início do código para auxiliar na criação das classes e na manipulação de datas.

- As classes foram criadas de acordo com o modelo de classes __UML__ e estão listadas abaixo:

    1. class Cliente
    2. class PessoaFisica(Cliente)
    3. class Conta
    4. class ContaCorrente(Conta)
    5. class Historico
    6. class Transacao(ABC)
    7. class Saque(Transacao)
    8. class Deposito(Transacao)


### 4.2 Arquivo main.py

- Os módulos __classes__ e __textwrap__ foram importados no início do código para utilizar as classes criadas no arquivo __classes_op.py__ e para formatar o texto exibido no terminal.

- No próximo passo foi criada uma mensagem de boas vindas e em seguida declaradas todas as funções que serão chamadas para execução do sistema. Vide lista de todas as funções criadas:

    01. def menu() - Função para listar as opções de menu.
    02. def filtrar_cliente(cpf, clientes) - Função para filtar e verificar se o cliente já está cadastrado.
    03. def recuperar_conta_cliente(cliente) - Função para verificar se o cliente possuí conta.
    04. def depositar(clientes) - Função para realizar depositos na conta do cliente.
    05. def sacar(clientes) - Função para realizar saques da conta do cliente.
    06. def exibir_extrato(clientes) - Função para exibir o extrato bancário da conta do cliente.
    07. def criar_cliente(clientes) - Função para cadastrar novos clientes.
    08. def criar_conta(numero_conta, clientes, contas) - Função para cadastrar nova conta para o cliente.
    09. def listar_contas(contas) - Função para listar todas as contas cadastradas.
    10. def main() - Função principal.

- Na última linha do código, é chamada a função "main()" para que o código seja executado.

## 5. Testes

O sistema bancário se comportou da maneira esperada, sempre pedindo o número de CPF para verificar se o cliente está cadastrado e se possuí conta para realzar as operações de deposito, saque e extrato. A função "listar_contas" também funcionou, listando todas as contas cadastradas.

__1º teste:__ Realização de cadastro de clientes, cadastro de contas e apresentação da lista de contas cadastradas. Cada nova conta cadastrada recebe um número em sequencia, com o cliente podendo ter várias contas. Vide __imagem 1__ abaixo mostrando o teste com as contas cadastradas:

<img src="images/imagem1.PNG"> Imagem 1


__2º teste:__ Testando as funções de deposito, saque e extrato. O sistema deve bloquear qualquer operação que fuja as regras do banco mencionadas anteriormente. Vide __imagem 2__ abaixo mostrando o teste das funções deposito, saque e extrato:

<img src="images/imagem2.PNG"> Imagem 2

## 6. Licença

Este projeto está licenciado sob a Licença Apache 2.0 - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 7. Conclusão

Este foi o meu terceiro projeto de __Liguagem Python__ dentro do curso __Python Development__ e confesso que foi muito mais desafiador que eu imaginei. Programar orientado a objetos esta sendo uma experiência de grande aprendizado e quero me aprofundar mais neste paradigma de programação.
Grande abraço a todos!!!
