from abc import ABC, abstractstaticmethod, abstractproperty
from datetime import datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas= []

    def realizar_transacao(self, conta, trasacao):
        self.contas= conta

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = 0
        self._agencia = "01"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta (cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo (self):
        return self._saldo
    
    @property
    def numero (self):
        return self._numero
    
    @property
    def agencia (self):
        return self._agencia
    
    @property
    def cliente (self):
        return self._cliente
    
    @property
    def historico (self):
        return self._historico
    
    def sacar (self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo 

        if excedeu_saldo:
            print("Sem Saldo Suficiente !!!")

        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado Com sucesso!")
            return True
        
        else:
            print (" Valor informado é invalido")

        return False
    
    def depositar (self, valor):
        if valor > 0 :
            self._saldo += valor
            print("Deposito realizado !")
        else:
            print("Operacao Falhou")
            return False
        
        return True
    