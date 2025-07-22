from tkinter import *
from functools import partial
class Arvore(Frame):
    def __init__(self, parent, controller,materia):
        self.__controller = controller
        self.__materia = materia
        Frame.__init__(self, parent)
        self.__botoes = []
        label = Label(self, text="arvore")
        label.grid(column=0, row=0)
        self.mostra()

    def mostra(self):
        for i in range(len(self.__botoes)):
            self.__botoes[i].destroy()
        self.__botoes.clear()
        materias = self.__controller.get_materias()
        fase_atual = 0
        temp = 2

        for i in materias.keys():
            materia = materias[i]
            if materia.get_concluida():
                cor = "green"
            elif materia.get_block():
                cor = "red"
            else:
                cor = "blue"
            if materia.testa_requisito(self.__materia.get_codigo()):
                x = Button(self, text=materia.get_codigo(), width=20,command=partial(self.__controller.tela_materia,materia),bg=cor)
                self.__botoes.append(x)
                if materia.get_fase() != fase_atual:
                    temp = 2
                    fase_atual = materia.get_fase()
                    label = Label(self, text=("fase",fase_atual))
                    label.grid(column=materia.get_fase()-1,row = temp-1)
                x.grid(column=materia.get_fase()-1,row = temp)
                temp += 1