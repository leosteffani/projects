from PyPDF2 import *
from io import StringIO
from pessoa import Pessoa
from materia import Materia
class Leitor():
    def __init__(self,pdf):
        self.__pessoa = Pessoa("eu")
        self.__arquivo = open(pdf, 'rb')
        self.__pdf = PdfReader(self.__arquivo)
        self.__paginas = self.__pdf.pages
    def le(self):
        for i in range(len(self.__paginas)):
            self.__linhas = []
            content = self.__paginas[i].extract_text()
            buf = StringIO(content)
            x =True
            indice = 0
            while x:
                x = buf.readline()
                x = x.replace('\n', ' ').replace('\r', '')
                self.__linhas.append(x)
                if len(x) >= 3:
                    #15
                    fase = ""
                    if len(x) > 12:
                        for h in range(12):
                            fase += x[h]
                    if fase == "ConjuntoFase" or fase == "ConjuntoCarg":
                        try:
                            nfase = x[len(x)-2]
                            nfase = int(nfase)
                        except:
                            nfase = 8
                    if x.find("Ob ") != -1:
                        ob = x.find("Ob ")
                        comeco = ob+3
                        codigo = ""
                        espaco = False
                        for i in range(7):
                            if x[comeco+i] == " ":
                                espaco = True
                            codigo += x[comeco+i]
                        if espaco:
                            continue
                        comeco += 10
                        nome = ""
                        ponto_de_quebra = len(x)-1
                        if x.find(" eh ") != -1:
                            ponto_de_quebra = x.find(" eh ")
                        elif x.find(" ou ") != -1:
                            ponto_de_quebra = x.find(" ou ")
                        for temp in range(comeco,ponto_de_quebra):
                            nome += x[temp]
                        analise = ""
                        for i in range(4):
                            analise += nome[len(nome) - i - 1]
                        try:
                            analise = int(analise)
                            nome = list(nome)
                            for i in range(7):
                                nome.pop()
                            nome = "".join(nome)
                        except ValueError:
                            pass

                        requisitos = []
                        if x.find("Ob ") == 8:
                            requisitos.append("")
                            for i in range(7):
                                requisitos[0] += x[i]
                        conta_ou = 0
                        roda = 1
                        while True:
                            if indice != 0:
                                anterior = self.__linhas[indice - roda]
                                eh = anterior.find("eh ")
                                ou = anterior.find("ou ")
                                if eh != -1:
                                    comeco = eh+3
                                    requisitos.append("eh ")
                                    if anterior[comeco] == "(":
                                        comeco +=1
                                    for i in range(7):
                                        requisitos[roda] += anterior[comeco + i]
                                    roda += 1
                                elif ou != -1:
                                    conta_ou += 1
                                    comeco = ou + 3
                                    requisitos.append("ou ")
                                    if anterior[comeco] == "(":
                                        comeco +=1
                                    for i in range(7):
                                        requisitos[roda] += anterior[comeco + i]
                                    roda += 1
                                else:
                                    break
                        inicio = 0
                        requisitos_final = []
                        for i in range(conta_ou+1):
                            requisitos_final.append([])
                        for i in range(len(requisitos)):
                            if requisitos[i][0] == "o":
                                inicio += 1
                            if requisitos[i][0] == "e" or requisitos[i][0] == "o":
                                x = list(requisitos[i])
                                x.pop(0)
                                x.pop(0)
                                x.pop(0)
                                requisitos[i] = "".join(x)
                            requisitos_final[inicio].append(requisitos[i])
                        self.__pessoa.add_materia(Materia(codigo,nome,requisitos_final,nfase))
                indice += 1
        self.__arquivo.close()
        return self.__pessoa
    def mostra(self):
        temp = self.__pessoa.get_materias()
        for i in temp:
            print(temp[i].get_codigo(),temp[i].get_nome(),temp[i].get_requisitos())
x = Leitor("curriculo.pdf")
x.le()
x.mostra()