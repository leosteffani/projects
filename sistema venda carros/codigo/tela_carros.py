from tkinter import *
from functools import partial
class Tela_carros(Frame):

    def __init__(self, parent, controller):
        self.__controller = controller
        Frame.__init__(self, parent)
        label = Label(self, text='digite a marca desejada\ndigite "todos" para ver todos os carros do estoque')
        label.pack(pady=10, padx=10)
        self.__pesquisa = Entry(self, width=20)
        self.__pesquisa.insert(0, '')
        self.__pesquisa.pack(padx=5, pady=5)
        botao_pesquisa = Button(self, text="procurar", width=20, command=self.mostra).pack()
        self.__botoes = []
        self.calcula_media()

    def mostra(self):
        for i in range(len(self.__botoes)):
            self.__botoes[i].destroy()
        self.__botoes.clear()
        marca = self.__pesquisa.get()
        carros = self.__controller.get_carros()
        for i in range(len(carros)):
            if marca == "todos" or carros[i].get_marca() == marca:
                produto = carros[i]
                x = Button(self, text=produto.get(), width=100,command=partial(self.__controller.tela_carro,produto))
                self.__botoes.append(x)
                x.pack()

    def calcula_media(self):
        soma = 0
        carros = self.__controller.get_carros()
        for i in range(len(carros)):
            soma += float(carros[i].get_preco())
        if len(carros) > 0:
            media = soma/len(carros)
        else:
            media = 0.0
        label = Label(self, text="média de preços: " + str(int(media)))
        label.pack(pady=10, padx=10)
