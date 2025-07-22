from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import time
import pickle
import shutil
class Tela_att(Frame):
    def __init__(self, parent, controller):
        self.__controller = controller
        Frame.__init__(self, parent)

        ms = Label(self, text='escolha o arquivo que desejar')
        ms.pack()

        msbtn = Button(self, text='Choose File', command=lambda: self.open_file())
        msbtn.pack()

        upld = Button(self, text='Upload Files', command=self.uploadFiles)
        upld.pack()

    def open_file(self):
        self.__file_path = askopenfile(mode='r', filetypes=[('PDF Files', '*pdf')])
        if self.__file_path is not None:
            Label(self, text='aquivo selecionado', foreground='green').pack()
        else:
            Label(self, text='falhou', foreground='red').pack()

    def uploadFiles(self):

        shutil.copyfile(self.__file_path.name, "curriculo.pdf")
        pb1 = Progressbar(self,orient=HORIZONTAL,length=300,mode='determinate')
        pb1.pack()
        for i in range(5):
            self.update_idletasks()
            pb1['value'] += 20
            time.sleep(1)
        pb1.destroy()
        Label(self, text='curriculo atualizado!,reinicie o app para atualizar', foreground='green').pack()
        Button(self, text='FECHE AQUI', command=self.fecha).pack()

    def fecha(self):
        try:
            self.__controller.abre_curriculo()
            self.__controller.fecha()
        except
            self.__controller.fecha()
