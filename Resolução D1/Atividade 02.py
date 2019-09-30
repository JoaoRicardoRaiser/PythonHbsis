# Criar um programa que utilize o método 50-20-10-20: (PaginaSobreMetodos)
# 1. Leia o salário líquido informado pelo usuário.
# 2. Organize os valores de acordo com o método citado.
# 3. Informe ao usuário qual o valor que ele deve destinar para cada categoria.

print("="*60)
salario = float(input("Digite o salário líquido: "))

print("{}O salário líquido é:{}R${:5.2f}".format(" "*5," "*12,salario))
print("{}Gasto essêncial:{}R${:5.2f}".format(" "*5," "*16, salario * 0.5))
print("{}Investimentos LP:{}R${:5.2f}".format(" "*5," "*15, salario * 0.2))
print("{}Investimentos CP:{}R${:5.2f}".format(" " * 5," "*15, salario * 0.1))
print("{}Livre:{}R${:5.2f}".format(" " * 5," "*15, salario *0.2))

print("="*60)

