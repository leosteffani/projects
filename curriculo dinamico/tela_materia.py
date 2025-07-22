from tkinter import *
class Tela_materia(Frame):
    def __init__(self, parent, controller,materia):
        self.__controller = controller
        self.__materia = materia
        Frame.__init__(self, parent)

        label = Label(self,text=self.__materia.get_nome())
        label.pack()
        #label = Label(self,text=("requisitos:",self.__materia.get_requisitos()))
        #label.pack()
        label = Label(self, text=("requisitos a concluir:", self.__materia.get_requisitos()))
        label.pack()
        self.__var = BooleanVar()
        self.__var.set(materia.get_concluida())
        c1 = Checkbutton(self, text='concluida?', variable=self.__var, onvalue=True, offvalue=False)
        c1.pack()

        button = Button(self, text="concluir", width=20,command=self.concluir)
        button.pack()
        button = Button(self, text="arvore de requisito", width=20, command=self.arvore)
        button.pack()
    def concluir(self):
        if not self.__materia.get_block():
            print("concluiu")
            self.__materia.set_concluida(self.__var.get())
            self.__controller.att_concluida(self.__materia,self.__var.get())
            if self.__var.get():
                self.__controller.libera_exigidos(self.__materia.get_codigo())
    def arvore(self):
        self.__controller.tela_arvore(self.__materia)