# Criar um programa que:
# 1. Cadastre usuário e senha.
# 2. Liste usuários cadastrados e suas respectivas senhas.
# 3. Efetue login, validando usuário e senha.
# Obs: O programa deve apresentar um menu para que o usuário possa realizar a ação que
# desejar e no momento em que desejar.

login = []
senha = []

resposta = "s"
while resposta == "s":
    print(" " * 60)
    login.append(input("Cadastre o login: "))
    senha.append(input("Cadastre a senha: "))
    print("")
    resposta = input("Deseja realizar mais algum cadastro? ")

for i in range(0,3):
    resposta_login = input("Digite seu login: ")
    resposta_senha = input("Digite sua senha: ")
    if resposta_login == login[i] and resposta_senha == senha[i]:
        print("Acesso concedido.")
        break
    else:
        print("Login / senha inválida!")
        print("")
        resposta_login = input("Digite seu login: ")
        resposta_senha = input("Digite sua senha: ")

    print("Acesso negado.")

print("Digite qualquer tecla para sair.")
input()
