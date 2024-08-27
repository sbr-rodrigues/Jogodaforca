import random
from os import system, name
def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system ('clear')

board = ['''
         _________
         |        |
         |
         |
         |
         |
         |
         |
         |________''',
         
         '''
         ________
         |       |
         |      (¨)
         |
         |
         |
         |
         |
         |________''',

         '''
         _________
         |        |
         |       (¨)
         |        |
         |        |
         |
         |
         |
         |_________''',

         '''
         ________
         |       |
         |     \(¨)
         |      \|
         |       |
         |
         |
         |
         |________''',
         
         '''
         ________
         |       |
         |     \(¨)/
         |      \|/
         |       |
         |
         |
         |
         |_________''',
         
         '''
        _________
        |        |
        |      \(¨)/
        |       \|/
        |        |
        |       /
        |      /
        |
        |__________''',
        
        '''
        _________
        |        |
        |      \(¨)/
        |       \|/
        |        |
        |       / \\
        |      /   \\
        |
        |__________'''
        ]

class Hangman:
    def __init__(self, palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_escolhidas = []

    def guess (self, letra):
    
        if letra in self.palavra and letra not in self.letras_escolhidas:
            self.letras_escolhidas.append(letra)
    
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True
    def hangman_over(self):
        return self.hangman_won() or (len(self.letras_erradas) == 6)
    
    def hangman_won(self):
        if ' _ ' not in self.hide_palavra():
            return True
        return False
    def hide_palavra(self):
        rtn = ' '
        for letra in self.palavra:
            if letra not in self.letras_escolhidas:
                rtn += ' _ '
            else:
                rtn += letra
        return rtn
    def print_game_status(self):
        print(board[len(self.letras_erradas)])
        print('\nPalavra: ' + self.hide_palavra())
        print('\nLetras erradas: ',)
        for letra in self.letras_erradas:
            print(letra,)
        print()
        print('Letras corretas: ',)
        print()
        for letra in self.letras_escolhidas:
            print(letra,)
        print()
           
def rand_palavra():
    print('¨'*20)
    print('{:^10}'.format('\033[4;33mHangman\033[m'))
    print('¨'*20)
    while True:
        print('\nBem-vindo(a) ao Jogo da forca')
        print('\nEscolha a categoria: ')
        print('1 - Carro')
        print('2 - Filme')
        print('3 - Fruta')
        print('4 - País')
        print('5 Sair do jogo')
        escolha = input('Escolha a opção: ')
        if escolha == '1':
            palavras = ['FUSCA', 'GOL', 'UNO', 'MOBI','ALFAROMEO', 'JAGUAR','ONIX','FORDKA','KWID','SONATA', 'ETIOS','MARCH','PRISMA','FERRARI','LAMBORGHINI','ARGO']
            palavra = random.choice(palavras)
            return palavra
        elif escolha == '2':
            palavras =['DEADPOOL','OCHAMADO','AMALDICAO','BATERECORRER','POLTERGEIST','ORGULHOEPRECONCEITO','ACOLINAESCARLATE','TITANIC', 'EOVENTOLEVOU', 'CASANOVA', 'ZORRO', 'DRACULA', 'HARRYPOTTEREAPEDRAFILOSOFAL', 'STARTREK', 'STARWAR','SHERK', 'AFREIRA', 'AFANTÁSTICAFÁBRICADECHOCOLATE', 'TUBARÃO']
            palavra = random.choice(palavras)
            return palavra
        elif escolha == '3':
            palavras = ['BANANA', 'MACA', 'MELANCIA','ABRICO','AMEIXA', 'JACA','PESSEGO', 'MELANCIA','MARMELO', 'PERA', 'LARANJA', 'CACAU', 'CAJU', 'ABACATE', 'MORANGO', 'ABACAXI', 'PINHA', 'MAMAO', 'KIWI','LIMAO']
            palavra = random.choice(palavras)
            return palavra
        elif escolha == '4':
            palavras = ['BRASIL', 'ARGENTINA', 'PERU', 'CHILE', 'VENEZUELA', 'CHINA', 'SKINLANKA', 'PAQUISTAO', 'DUBAI','CONGO','NORUEGA','DINAMARCA','INGLATERRA']
            palavra = random.choice(palavras)
            return palavra
        elif escolha == '5':
            print('Saindo do Jogo')
            break
        else: 
            print('Opção inválida! Por favor, escolha uma opção válida')
def main ():
    limpa_tela()
    game = Hangman(rand_palavra())
    while not game.hangman_over():
        game.print_game_status()
        user_input = input('\nDigite uma letra: ').upper()
        game.guess(user_input)
    game.print_game_status()
    if game.hangman_won():
        print('\nParabéns! Você ganhou!')
    else:
        print('\nGame Over!')
        print('A palavra era ' + game.palavra)
    print('\nFoi bom jogar com você!\n')
if __name__ == "__main__":
    main()