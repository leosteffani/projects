from tkinter import *
from tela_add_carro import Tela_add_carro
from tela_carros import Tela_carros
from tela_carro import Tela_carro
import pickle

class Main():
    def __init__(self):
        self.__carros = pickle.load( open( "save.pkl", "rb" ))
        self.__janela = Tk()
        self.__janela.geometry("800x600")
        self.__container = Frame(self.__janela)
        self.__container.pack(side="top", fill="both", expand=True)

        self.__container.grid_rowconfigure(0, weight=800)
        self.__container.grid_columnconfigure(0, weight=600)

        self.__menu = Menu(self.__container, tearoff=0)
        self.__menu.add_command(label="Adicionar", command=self.tela_add_carro)
        self.__menu.add_command(label="Carros",command= self.tela_carros)

        self.__telas_carros = {}

        self.__janela.config(menu=self.__menu)

        self.__janela.protocol("WM_DELETE_WINDOW", self.fecha)
        self.__janela.mainloop()

    def get_carros(self):
        return self.__carros

    def fecha(self):
        pickle.dump( self.__carros, open( "save.pkl", "wb" ))
        self.__janela.destroy()

    def add_carro(self,carro_novo):
        self.__carros.append(carro_novo)

    def remove_carro(self,carro):
        self.__carros.remove(carro)

    def cria_telas_carros(self):
        for i in range(len(self.__carros)):
            self.__telas_carros[self.__carros[i]] = Tela_carro(self.__container, self,self.__carros[i])

    def tela_carro(self,carro):
        frame = self.__telas_carros[carro]
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def tela_add_carro(self):
        frame = Tela_add_carro(self.__container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def tela_carros(self):
        self.cria_telas_carros()
        frame = Tela_carros(self.__container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

main = Main()
