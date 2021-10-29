class Conta:
    def __init__(self,numero,titular, saldo):
        print("Construindo objeto...".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo

    @property
    def nome(self,nome):
        return self.__nome.title()

    @nome.setter
    def __int__(self, nome):
        self.__nome = nome

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo,self.__titular))

    def deposita(self,valor):
        self.__saldo += valor
        print("Deposito concluido com sucesso.")

    def check_saldo(self, valor_debitar):
        return valor_debitar <= self.__saldo

    def saca(self,valor):
        if (self.check_saldo(valor)):
            self.__saldo -= valor
        else:
            print("Saldo insuficiente. Voce tem {}".format(self.__saldo))

    def transfere(self,valor,destino):
        if(self.check_saldo(valor)):
            self.saca(valor)
            destino.deposita(valor)
        else:
            print("Saldo insuficiente.Voce tem {}.".format(self.__saldo))

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def numero(self):
        return self.__numero

    @staticmethod
    def codigo_banco():
        return "001"

