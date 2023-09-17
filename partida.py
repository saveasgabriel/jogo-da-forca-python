import jogo

aleatorio = jogo.PalavraAleatoria()
palavra_secreta = aleatorio.definir_palavra()
partida = jogo.JogoDaForca(palavra_secreta)
cont = 0

while not partida.verificar_derrota() and not partida.verificar_vitoria():
    cont += 1

    # Mostra o número da rodada
    print(f"\n------------- Rodada n° {cont} ----------------")

    # Mostra as chances restantes
    partida.mostrar_chances()

    # Mostra a representação visual da forca
    partida.mostrar_forca()

    # Mostra a palavra oculta com letras adivinhadas
    partida.mostrar_palavra()

    # Solicita ao jogador a próxima letra
    letra = input("Digite aqui a próxima letra: ")

    # Processa a adivinhação do jogador
    partida.advinhar(letra)

print("\n Fim da Partida!\n")

if partida.verificar_vitoria():
    print(f"Parabéns, você acertou tudo! A palavra é mesmo \"{palavra_secreta}\".")
else:
    print(f"Que pena, você foi enforcado! A palavra era \"{palavra_secreta}\".")
