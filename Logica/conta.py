numero_banco = 10


def cria_conta(nome, numero_conta, saldo):   
    return {'nome':nome, 'numero_c':numero_conta, 'saldo':saldo }

def depositar(cnt, valor):
    cnt['saldo'] += valor
    
def sacar(cnt,valor):
    cnt['saldo'] -= valor

def mostrar_numero_banco():
    print(numero_banco)

mostrar_numero_banco()
