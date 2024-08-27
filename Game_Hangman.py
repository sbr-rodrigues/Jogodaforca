import random
from os import system, name
def limpa_tela():
    if name == 'nt':
        _ = system ('cls')
    else:
        _ = system ('clear')

def game():
    limpa_tela()
    
    print('\nBem-vindo(a) ao jogo da forca!')
    print('Advinhe a palavra abaixo:\n')
    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']
    palavra = random.choice (palavras)
    letras_descobertas = ['_' for letra in palavra]
    chances = 6
    letras_erradas = []

    while chances > 0:
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))
        tentativa = input ("\nDigite uma letra: ").lower()
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas [index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)
        if "_" not in letras_descobertas:
            print("\nVocê venceu, a palavra era:", palavra)
            break
    if "_" in letras_descobertas:
        print("\nVocê perdeu, a palavra era:", palavra)

game()
   


