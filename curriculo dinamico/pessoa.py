class Pessoa():
    def __init__(self,nome):
        self.__nome = nome
        self.__materias = {}

    #getters
    def get_nome(self):
        return self.__nome
    def get_materias(self):
        return self.__materias

    #setters
    def set_nome(self,nome):
        self.__nome = nome

    def add_materia(self,materia):
        self.__materias[materia.get_codigo()] = materia

    def att_concluida(self,materia,conclui):
        self.__materias[materia.get_codigo()].set_concluida(conclui)

    def libera(self,codigo):
        for x in self.__materias.keys():
            self.__materias[x].elimina_requisito(codigo)

