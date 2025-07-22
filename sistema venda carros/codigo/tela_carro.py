from tkinter import *
class Tela_carro(Frame):
    def __init__(self, parent, controller,produto):
        self.__controller = controller
        self.__produto = produto
        Frame.__init__(self, parent)

        self.__marca = Label(self, text="marca: " + produto.get_marca())
        self.__marca.pack(pady=10, padx=10)

        self.__modelo = Label(self, text="modelo: " + produto.get_modelo())
        self.__modelo.pack(pady=10, padx=10)

        self.__ano = Label(self, text="ano: " + produto.get_ano())
        self.__ano.pack(pady=10, padx=10)

        self.__preco = Label(self, text="preço: " + produto.get_preco())
        self.__preco.pack(pady=10, padx=10)

        self.__usado = Label(self,text= produto.get_usado_escrito())
        self.__usado.pack(pady=10, padx=10)

        Label(self, text="--------------------------------------------------").pack(pady=10, padx=10)

        self.__nova_marca = Entry(self, width=20)
        self.__nova_marca.insert(0, 'atualizar marca')
        self.__nova_marca.pack(padx=5, pady=5)

        self.__novo_modelo = Entry(self, width=20)
        self.__novo_modelo.insert(0, 'atualizar modelo')
        self.__novo_modelo.pack(padx=5, pady=5)

        self.__novo_ano = Entry(self, width=20)
        self.__novo_ano.insert(0, 'atualizar ano')
        self.__novo_ano.pack(padx=5, pady=5)

        self.__novo_preco = Entry(self, width=20)
        self.__novo_preco.insert(0, 'atualizar preço')
        self.__novo_preco.pack(padx=5, pady=5)

        Label(self, text="atualizar estado:").pack(pady=10, padx=10)

        self.__novo_usado = BooleanVar()
        self.__novo_usado.set(False)

        RBttn = Radiobutton(self, text="Novo", variable=self.__novo_usado,
                            value=False)
        RBttn.pack(padx=5, pady=5)
        RBttn2 = Radiobutton(self, text="Usado", variable=self.__novo_usado,
                             value=True)
        RBttn2.pack(padx=5, pady=5)

        atualiza = Button(self, text="Atualizar dados",command=self.atualiza).pack()

        self.__erro = Label(self, text="")
        self.__erro.pack(pady=10, padx=10)

        Label(self, text="").pack(pady=10, padx=10)

        remove = Button(self, text="Remover carro",command=self.remove).pack()

    def atualiza(self):
        marca = self.__nova_marca.get()
        modelo = self.__novo_modelo.get()
        ano = self.__novo_ano.get()
        preco = self.__novo_preco.get()
        usado = self.__novo_usado.get()

        if marca != "atualizar marca":
            self.__produto.set_marca(marca)
        if modelo != "atualizar modelo":
            self.__produto.set_modelo(modelo)
        if ano != "atualizar ano":
            self.__produto.set_ano(ano)
        if preco != "atualizar preço":
            self.__produto.set_preco(preco)
        self.__produto.set_usado(usado)

        self.__erro.after(1000, self.__erro.destroy())
        self.__erro = Label(self, text="Dados atualizados")
        self.__erro.pack(pady=10, padx=10)
        self.__controller.tela_carros()

    def remove(self):
        self.__controller.remove_carro(self.__produto)
        self.__controller.tela_carros()