from conta import Conta
from data import Data

conta_0 = Conta(123,"Ana",500)
conta_1 = Conta(456,"Joao",500)

print("Banco {}".format(Conta.codigo_banco()))

print("Conta 0:\nTitular: {}\nNumero: {}\nSaldo: {}\n".format(
    conta_0.titular,conta_0.numero,conta_0.saldo))

print("Conta 1:\nTitular: {}\nNumero: {}\nSaldo: {}\n".format(
    conta_1.titular,conta_1.numero,conta_1.saldo))

conta_0.transfere(4000,conta_1)

