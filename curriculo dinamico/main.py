from tkinter import *
from tela_curriculo import Tela_curriculo
from tela_materia import Tela_materia
from leitorPDF import Leitor
from arvore import Arvore
from att import Tela_att
import pickle

class Main():
    def __init__(self):
        self.__leitor = Leitor("curriculo.pdf")
        self.__pessoa = pickle.load(open('save.pkl', 'rb'))
        #self.__pessoa = self.__leitor.le()
        print(self.__pessoa.get_nome())
        self.__janela = Tk()
        self.__janela.geometry("1920x1080")
        self.__janela.attributes('-fullscreen', True)
        self.__container = Frame(self.__janela)

        self.__container.pack(side="top", fill="both", expand=True)
        self.__container.grid_rowconfigure(0, weight=800)
        self.__container.grid_columnconfigure(0, weight=600)

        self.__menu = Menu(self.__container, tearoff=0)
        self.__menu.add_command(label="curriculo", command=self.tela_curriculo)
        self.__menu.add_command(label="atualizar", command=self.tela_att)
        self.__menu.add_command(label="fechar",command=self.fecha)

        self.__janela.config(menu=self.__menu)
        self.__telas_materias = {}
        self.cria_telas_materias()

        self.__janela.protocol("WM_DELETE_WINDOW", self.fecha)
        self.__janela.mainloop()


    def abre_curriculo(self):
        self.__pessoa = self.__leitor.le()
        return self.__pessoa

    def get_pessoa(self):
        return self.__pessoa

    def get_materias(self):
        return self.__pessoa.get_materias()

    def reinicia(self):
        pickle.dump(self.__pessoa, open("save.pkl", "wb"))
        x = self
        self.__janela.destroy()
        x.__init__()
        print("salvou")

    def fecha(self):
        pickle.dump( self.__pessoa,open( "save.pkl", "wb" ))
        self.__janela.destroy()
        print("salvou")

    def att_concluida(self,materia,y):
        self.__pessoa.att_concluida(materia,y)

    def libera_exigidos(self,codigo):
        self.__pessoa.libera(codigo)

    def cria_telas_materias(self):
        for i in self.__pessoa.get_materias().keys():
            self.__telas_materias[self.__pessoa.get_materias()[i]] = Tela_materia(self.__container, self,self.__pessoa.get_materias()[i])

    def tela_materia(self,materia):
        frame = Tela_materia(self.__container, self,materia)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def tela_arvore(self,materia):
        frame = Arvore(self.__container, self,materia)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def tela_curriculo(self):
        frame = Tela_curriculo(self.__container,self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def tela_att(self):
        frame = Tela_att(self.__container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()
main = Main()
