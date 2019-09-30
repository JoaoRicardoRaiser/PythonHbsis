#1. Leia uma frase digitada pelo usuário.
#2. Leia uma letra digitada pelo usuário.
#3. Informe para o usuário quantas vezes aparece na frase (passo 1) a letra (passo 2).
#4. Informe para o usuário a posição em que a letra aparece a primeira vez na frase.
#5. Informe para o usuário a posição em que a letra aparece pela última vez na frase.
print('=' * 60)
frase = input("Digite uma frase: ")
letra = input("Digite uma letra: ")

print("{}A letra foi encontrada {} vezes.".format(" "*20,frase.count(letra))) #A função COUNT faz a contagem da quantidade da letra escolhida, que está presente na frase digitada.
print("{}A letra foi encontrada pela primeira vez na posição: {}".format(" "*20,frase.index(letra))) #A função INDEX procura a primeira posição em que a letra escolhida apareceu.
print("{}A letra foi encontrada pela ultima vez na posição: {}".format(" "*20,frase.rindex(letra))) #A função RINDEX procura a última posição em que a letra escolhida apareceu.
print("=" * 60)