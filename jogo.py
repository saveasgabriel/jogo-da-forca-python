import random

class JogoDaForca:
    def __init__(self, palavra_secreta):
        # Inicializa os atributos da classe
        self.letras_corretas = []
        self.letras_erradas = []
        self.chances_restantes = 6
        self.palavra_secreta = palavra_secreta

    def advinhar(self, letra):
        # Verifica se a letra está na palavra secreta e atualiza as listas
        if letra in self.palavra_secreta:
            self.letras_corretas.append(letra)
        else:
            self.letras_erradas.append(letra)
            self.chances_restantes -= 1

    def mostrar_palavra(self):
        # Mostra a palavra com letras corretas adivinhadas e '_' para as não adivinhadas
        resultado = ''
        for letra in self.palavra_secreta:
            if letra in self.letras_corretas:
                resultado += letra
            else:
                resultado += '_'
        print(f"Palavra:{resultado}\n")

    def mostrar_forca(self):
        # Mostra a representação visual da forca de acordo com as chances restantes
        partes_forca = [
            "|-------",
            "|      |",
            "|      o",
            "|     /|\\",
            "|     / \\",
            "|"
        ]

        for i in range(6 - self.chances_restantes):
            print(partes_forca[i])

    def verificar_vitoria(self):
        # Verifica se todas as letras da palavra secreta foram adivinhadas corretamente
        return all(letra in self.letras_corretas for letra in self.palavra_secreta)

    def verificar_derrota(self):
        # Verifica se o jogador perdeu (chances esgotadas)
        return self.chances_restantes <= 0

    def mostrar_chances(self):
        # Mostra quantas chances restantes o jogador tem
        print(f"Você possui um total de {self.chances_restantes} chances restantes\n")


class PalavraAleatoria:
    def __init__(self):
        # Inicializa a lista de palavras
        self.lista_palavras = [
            "casa", "gato", "amigo", "sol", "rio", "festa", "livro", "bola", "carro", "chuva",
            "dia", "noite", "mar", "vento", "comida", "escola", "trabalho", "jogo", "música", "cor",
            "cidade", "viagem", "família", "cachorro", "computador", "telefone", "papel", "tempo", "dinheiro",
            "mãe", "pai", "irmão", "irmã", "avô", "avó", "criança", "janela", "porta", "praia",
            "montanha", "floresta", "lua", "estrela", "frio", "calor", "amor", "odiar", "sorrir", "chorar",
            "correr", "andar", "nadar", "cozinhar", "ler", "escrever", "estudar", "aprender", "ensinar", "viajar",
            "sonhar", "acordar", "dormir", "feliz", "triste", "pequeno", "grande", "novo", "velho", "bonito",
            "feio", "bom", "ruim", "vermelho", "azul", "verde", "amarelo", "preto", "branco", "roxo",
            "laranja", "rosa", "cinza", "doce", "azedo", "salgado", "frio", "quente", "macio", "duro",
            "doente", "saudável", "rico", "pobre", "alto", "baixo", "rápido", "lento", "barulhento", "silencioso"
        ]

    def definir_palavra(self):
        # Escolhe aleatoriamente uma palavra da lista
        palavra = random.choice(self.lista_palavras)
        return palavra
