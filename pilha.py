class pilha:
    def __init__(self):
        self.topo = None
        self.primeiro = None
        self.__tam = 0
        self.__ite = None

    class elemento:
        def __init__(self, x):
            self.conteudo = x
            self.proximo = None

    class STACK:
        def __init__(self):
            self.conteudo = None
            self.proximo = None

    def __getitem__(self, index):
        for i, e in enumerate(self):
            if i == index:
                return e
        raise IndexError("List index out of range!")

    def __setitem__(self, index, value):
        for i, e in enumerate(self):
            if i == index:
                self.elemento = value
                return
        raise IndexError("List index out of range!")

    def __len__(self):
        return self.__tam

    def __str__(self):
        retorna = '['
        for i, e in enumerate(self):
            retorna += e.__repr__()
            if i < self.__tam - 1:
                retorna += ', '
        retorna += ']'
        return retorna

    def __repr__(self):
        return self.__str__()

    def iterar(self):
        if self.__ite is None:
            self.__ite = self.topo()
        else:
            self.__ite = self.__ite.proximo
        if self.__ite is not None:
            return self.__ite.conteudo

    def topo(self):
        return self.topo()

    def SIZE(self):
        return self.__tam

    def isEMPTY(self):
        if self.SIZE() == 0:
            return True
        else:
            return False

    def PUSH(self, x):
        novo = self.elemento(x)
        if self is None:
            self.topo = novo
            self.primeiro = novo
        else:
            self.topo.proximo = novo
            self.topo = self.topo.proximo
        self.__tam += 1
        self.__ite = None

    def POP(self):
        anterior = self.primeiro
        for i, e in enumerate(self):
            if i == self.SIZE() - 1:
                lixo = e
                self.topo = anterior
                self.topo.proximo = None
                return lixo
            if i > 0:
                anterior = anterior.proximo
        raise IndexError("Erro inesperado!")

