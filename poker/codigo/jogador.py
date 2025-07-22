class Jogador:
    def __init__(self, dinheiro):
        self.__dinheiro = dinheiro
        self.__mao = []
        self.__aposta = 0
        self.__jogando = True
#desistir da mao
    def fold(self):
        x = self.__aposta
        self.__aposta = 0
        self.__jogando = False
        return x
#aumentar a aposta anterior
    def raize(self):
        aumento = input("nova aposta:")
        self.__aposta = aumento
        return aumento

#pagar a aposta
    def pagar(self):
        self.__aposta =
