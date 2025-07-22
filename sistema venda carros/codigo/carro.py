class Carro():
    def __init__(self,marca,modelo,ano,preco,usado):
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = str(ano)
        self.__preco = float(preco)
        self.__preco = str(self.__preco)
        self.__usado = usado

    #getters
    def get_marca(self):
        return self.__marca
    def get_modelo(self):
        return self.__modelo
    def get_ano(self):
        return self.__ano
    def get_preco(self):
        return self.__preco
    def get_usado(self):
        return self.__usado

    def get_usado_escrito(self):
        if self.__usado:
            return "usado"
        return "novo"

    def get(self):
        return "marca:",self.__marca,"/modelo:",self.__modelo,"/ano:",self.__ano,"/preço:",self.__preco,"/",self.get_usado_escrito()

    #setters

    def set_marca(self,marca):
        self.__marca = marca
    def set_modelo(self,modelo):
        self.__modelo = modelo
    def set_ano(self,ano):
        self.__ano = ano
    def set_preco(self,preco):
        self.__preco = preco
    def set_usado(self,usado):
        self.__usado = usado