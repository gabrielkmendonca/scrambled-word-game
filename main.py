import random

def solicitar_lista_palavras():
    lista_palavras = []
    quantidade_palavras = int(input("\nInsira a quantidade de palavras (mín 10): "))
    print()
    
    if quantidade_palavras < 10:
        while quantidade_palavras < 10:
            quantidade_palavras = int(input("Quantidade inferior a necessária! Insira outro valor (mín 10): "))
    
    for i in range (quantidade_palavras):
        lista_palavras.append(input(f"Insira a {i+1}° palavra: "))   

    return lista_palavras


def sortear_palavra(lista_palavras):
    tamanho_lista = len(lista_palavras)
    indice_sorteado = random.randint(0, tamanho_lista-1)
    palavra_sorteada = lista_palavras[indice_sorteado]

    return palavra_sorteada


def embaralhar_palavra(palavra_sorteada):
    caracteres = []
    for i in palavra_sorteada:
        caracteres.append(i)

    n = len(caracteres)

    total_trocas = 2 * n -1
    contador_trocas = 0

    while contador_trocas < total_trocas:
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)

        if i != j:
            sup = caracteres[i]
            caracteres[i] = caracteres[j]
            caracteres[j] = sup
            contador_trocas += 1
        else:
            continue

    palavra_embaralhada = ""
    for letra in caracteres:
        palavra_embaralhada += letra

    return palavra_embaralhada


def jogar(palavra_sorteada, palavra_embaralhada):
    total_tentativas = 7
    tentativa_atual = 1

    print(f"\nA palavra embaralhada é: {palavra_embaralhada}")
    print("Você possui 7 tentativas ao todo. Boa sorte!\n")

    while tentativa_atual <= total_tentativas:
        palpite = input(f"Tentativa {tentativa_atual}/{total_tentativas} -> Digite seu palpite: ").strip()

        if palpite.lower() == palavra_sorteada.lower():
            print("\n🏆 Parabéns! Você acertou a palavra!")
            return True
        else:
            print("Palavra incorreta! Tente novamente. \n")
            tentativa_atual += 1

    return False

print("======= Jogo da Palavra Embaralhada =======")

lista_palavras = solicitar_lista_palavras()
palavra_sorteada = sortear_palavra(lista_palavras)
palavra_embaralhada = embaralhar_palavra(palavra_sorteada)
ganhou = jogar(palavra_sorteada, palavra_embaralhada)

if not ganhou:
    print("\n☠️  GAME OVER! Você não acertou a palavra.")
    print(f"A palavra era: {palavra_sorteada}")