import random
from os import system, name

def limpa_tela():
    if name =='nt':
      _ = system ('cls')
    else:
      _ = system ('clear')

def display_hangman(chances):
  stages = [ #Estágio 6 (final)    
            """
              ________
              |      |
              |      0
              |     \|/
              |     / \
              |
              ========
            """,
              #Estágio 5
            """
              ________
              |      | 
              |      0
              |     \|/
              |     /
              |      
              =======
              
            """,
            #Estágio 4
            """  
              ________
              |      | 
              |      0
              |     \|/
              |      
              |      
              =======
            
            """,
              #Estágio 3 
            """
              ________
              |      | 
              |      0
              |     \|
              |      
              |     
              =======
            """,
              #Estágio 2 
            """
              ________
              |      | 
              |      0
              |      |
              |      
              |     
              =======
            """,
              #Estágio 1
            """
              ________
              |      | 
              |      0
              |        
              |      
              |     
              =======
            """,
              #Estágio 0
            """
              ________
              |      | 
              |      
              |     
              |      
              | 
              =======
            """
  ]
  return stages [chances]


def game ():

  limpa_tela()

  print("-"*40)
  print("{:^40}".format("\033[32m Bem vindo ao jogo da forca!"))
  print("-"*40)
  while True:
    try:
      print("""\nEscolha a categoria: 
      [1] Carros
      [2] Filmes
      [3] Frutas
      [4] Roupas\033[m""")
      print("-"*40)
      opcao = int(input("\033[42;mQual é a opção? \033[m"))  
    except (ValueError, TypeError, SyntaxError):
      print("\n\033[31mUsuário preferiu não digitar este caracter\033[m]")
      return      
    if opcao == 1:
      palavras = ['FUSCA', 'VOLKSWAGENGOL', 'FIATUNO', 'CHEVROLETONIX', 'FORDKA', 'RENAULTKWID', 'TOYOTAETIOS', 'NISSANMARCH', 'CHEVROLETPRISMA','FERRARI','JAGAR','LAMBORGHINI', 'ALFAROMEO', 'FIATARGO']
      palavra = random.choice (palavras)
      lista_letras_palavras = [letra for letra in palavra]
      tabuleiro = ["_"] *len(palavra)
      chances = 6
      letras_tentativas = []
        
    elif opcao == 2:
      palavras = ['DEADPOOL','OCHAMADO','AMALDICAO','BATERECORRER','POLTERGEIST','ORGULHOEPRECONCEITO','ACOLINAESCARLATE','TITANIC', 'EOVENTOLEVOU', 'CASANOVA', 'ZORRO', 'DRACULA', 'HARRYPOTTEREAPEDRAFILOSOFAL', 'STARTREK', 'STARWAR','SHERK', 'AFREIRA', 'AFANTÁSTICAFÁBRICADECHOCOLATE', 'TUBARÃO']
      palavra = random.choice (palavras)
      lista_letras_palavras = [ letra for letra in palavra]
      tabuleiro = ["_"]*len(palavra)
      chances = 6
      letras_tentativas =[]

    elif opcao == 3:
      palavras = ['BANANA', 'MACA', 'MELANCIA','ABRICO','AMEIXA', 'JACA','PESSEGO', 'MELANCIA','MARMELO', 'PERA', 'LARANJA', 'CACAU', 'CAJU', 'ABACATE', 'MORANGO', 'ABACAXI', 'PINHA', 'MAMAO', 'KIWI','LIMAO']
      palavra = random.choice (palavras)
      lista_letras_palavras = [ letra for letra in palavra]
      tabuleiro = ["_"]*len(palavra)
      chances = 6
      letras_tentativas =[]

    elif opcao == 4:
      palavras = ['CAMISA', 'CAMISETA', 'GRAVATA', 'TERNO','SOBRETUDO','CUECA', 'CALCINHA', 'SUTIA', 'SAIA', 'JAQUETA', 'CACHECOL', 'CALÇA', 'CASACO', 'VESTIDO', 'SHORT', 'PIJAMA', 'MEIAS', 'MEIACALCA']
      palavra = random.choice (palavras)
      lista_letras_palavras = [letra for letra in palavra]
      tabuleiro = ["_"]*len(palavra)
      chances = 6
      letras_tentativas = []
    else:
      print('Opção inválida! Por favor, escolha uma opção válida.')
    while chances > 0:
      print (display_hangman(chances))
      print("Palavra: \n", tabuleiro)
      tentativa = input("\033[1;31;42m\nDigite uma letra: \033[m").upper()

      if tentativa in letras_tentativas:
        print ("\033[4;33mVocê já tentou essa letra, escolha outra!\033[m")
        continue
      letras_tentativas.append(tentativa) 

      if tentativa in lista_letras_palavras:
        print ("\033[4;32mVocê acertou a letra!\033[m")

        for indice in range (len(lista_letras_palavras)):
          if lista_letras_palavras [indice] == tentativa:
            tabuleiro[indice] = tentativa
        if "_" not in tabuleiro:
          print(f"\033[42mVocê venceu! A palavra era: {palavra}\033[m")
          break
      else:
        print("\033[33mOps! Esta letra não está na palavra!\033[m")
        chances -= 1
    if "_" in tabuleiro:
      print(f"\033[41mVocê perdeu! A palavra era: {palavra}\033[m")
    resp = " "
    while resp not in "S/N":
      resp = str(input("Quer continuar: [S/N]? ")).strip().upper()[0]
    if resp == "N":
      break


game( )


    