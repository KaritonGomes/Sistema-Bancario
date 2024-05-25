# Banco em Python

Este é um projeto de simulação de operações bancárias em Python, que permite a criação de clientes, contas, depósitos, saques e exibição de extratos.

## Funcionalidades

- Criação de novos clientes.
- Criação de novas contas.
- Realização de depósitos.
- Realização de saques.
- Exibição de extratos das contas.

## O Que Aprendi

### Programação Orientada a Objetos (POO)

1. **Encapsulamento**: Protegi os dados das classes usando métodos públicos e atributos privados.
2. **Herança**: Criei hierarquias de classes para compartilhar e estender funcionalidades, como `Cliente` e `PessoaFisica`, e `Conta` e `ContaCorrente`.
3. **Polimorfismo**: Utilizei classes abstratas e métodos para permitir que diferentes tipos de transações (`Saque` e `Deposito`) sejam tratados de maneira uniforme.
4. **Composição**: Reforcei a relação entre objetos, como `Conta` e `Historico`, e `Cliente` e `Conta`.

### Estrutura de Organização

1. **Modularidade**: Organizei o código em classes e métodos, facilitando a manutenção e o entendimento do código.
2. **Responsabilidade Única**: Segui o princípio da responsabilidade única, garantindo que cada classe e método tenha uma única responsabilidade clara.
3. **Leitura e Manutenção**: A estrutura do código foi planejada para ser clara e fácil de seguir, permitindo futuras extensões e melhorias sem complicações.

### Segurança

1. **Validação de Dados**: Implementei verificações de valores e limites em métodos de saque e depósito para prevenir operações inválidas.
2. **Controle de Acesso**: Usei encapsulamento para proteger dados sensíveis e métodos críticos de acesso direto e modificação.
3. **Registro de Transações**: Mantive um histórico detalhado de todas as transações realizadas para auditoria e acompanhamento.

## Classes e Estrutura

- `Cliente`: Classe base para clientes.
- `PessoaFisica`: Subclasse de Cliente para pessoas físicas.
- `Conta`: Classe base para contas bancárias.
- `ContaCorrente`: Subclasse de Conta para contas correntes.
- `Historico`: Armazena o histórico de transações de uma conta.
- `Transacao`: Classe abstrata para transações.
- `Saque`: Subclasse de Transacao para saques.
- `Deposito`: Subclasse de Transacao para depósitos.
