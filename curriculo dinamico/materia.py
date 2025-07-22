class Materia():
    def __init__(self,codigo,nome,requisitos,fase):
        self.__codigo = codigo
        self.__nome = nome
        self.__requisitos = requisitos
        self.__requisitos_completos = []
        for i in range(len(self.__requisitos)):
            self.__requisitos_completos.append(self.__requisitos[i])
        self.__fase = fase
        self.__concluida = False
        self.__block = True
        self.testa_liberar()

    #gettets
    def get_codigo(self):
        return self.__codigo
    def get_nome(self):
        return self.__nome
    def get_requisitos(self):
        return self.__requisitos
    def get_fase(self):
        return self.__fase
    def get_concluida(self):
        return self.__concluida
    def get_block(self):
        return self.__block
    def get_requisitos_completos(self):
        return self.__requisitos_completos

    def set_concluida(self,x):
        if x == True:
            if self.testa_liberar():
                self.__concluida = x

    def elimina_requisito(self,codigo):
        temp0 = self.__requisitos
        temp1 = self.__requisitos_completos
        for i in range(len(temp0)):
            for j in range(len(temp0[i])):
                if temp0[i][j] == codigo:
                    temp1[i].remove(codigo)
        self.testa_liberar()

    def testa_requisito(self,codigo):
        temp0 = self.__requisitos
        temp1 = self.__requisitos_completos
        for i in range(len(temp0)):
            for j in range(len(temp0[i])):
                if temp0[i][j] == codigo:
                    return True
        return False

    def testa_liberar(self):
        for i in range(len(self.__requisitos_completos)):
            if len(self.__requisitos_completos[i]) == 0:
                self.__block = False
                return True
        return False