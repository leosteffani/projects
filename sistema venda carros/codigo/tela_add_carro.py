from tkinter import *
from carro import Carro
class Tela_add_carro(Frame):
    def __init__(self, parent, controller):
        self.__controller = controller
        Frame.__init__(self, parent)

        self.__marca = Entry(self, width=20)
        self.__marca.insert(0, 'marca')
        self.__marca.pack(padx=5, pady=5)

        self.__modelo = Entry(self, width=20)
        self.__modelo.insert(0, 'modelo')
        self.__modelo.pack(padx=5, pady=5)

        self.__ano = Entry(self, width=20)
        self.__ano.insert(0, 'ano')
        self.__ano.pack(padx=5, pady=5)

        self.__valor = Entry(self, width=20)
        self.__valor.insert(0, 'Valor')
        self.__valor.pack(padx=5, pady=5)

        self.__Var1 = BooleanVar()
        self.__Var1.set(False)

        RBttn = Radiobutton(self, text="Novo", variable=self.__Var1,
                            value=False)
        RBttn.pack(padx=5, pady=5)
        RBttn2 = Radiobutton(self, text="Usado", variable=self.__Var1,
                             value=True)
        RBttn2.pack(padx=5, pady=5)

        Button(self, text="adicionar produto", width=20,
               command=lambda: self.add()).pack()
        self.__erro = Label(self, text="")
        self.__erro.pack(pady=10, padx=10)

    def add(self):
        try:
            produto = Carro(self.__marca.get(),self.__modelo.get(),int(self.__ano.get()),float(self.__valor.get()),self.__Var1.get())
            self.__controller.add_carro(produto)
            self.__erro.after(1000, self.__erro.destroy())
            self.__erro = Label(self, text="Carro adicionado com sucesso")
            self.__erro.pack(pady=10, padx=10)
        except ValueError:
            self.__erro.after(1000, self.__erro.destroy())
            self.__erro = Label(self, text="Algum valor foi inserido de maneira incorreta")
            self.__erro.pack(pady=10, padx=10)



