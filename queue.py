class queue:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.__tamanho = 0
        self.__ite = None

    class elemento:
        def __init__(self, x):
            self.conteudo = x
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
        return self.__tamanho

    def __str__(self):
        retorna = '['
        for i, e in enumerate(self):
            retorna += e.__repr__()
            if i < self.LEN() - 1:
                retorna += ', '
        retorna += ']'
        return retorna

    def __repr__(self):
        return self.__str__()

    def iterar(self):
        if self.__ite is None:
            self.__ite = self.primeiro
        else:
            self.__ite = self.__ite.proximo
        if self.__ite is not None:
            return self.__ite.conteudo

    def LEN(self):
        return self.__tamanho

    def ENQUEUE(self, x):
        novo = self.elemento(x)
        if self is None:
            self.primeiro = novo
            self.ultimo = novo

        else:
            self.ultimo.proximo = novo

        self.__tamanho += 1
        self.__ite = None

    def DENQUEUE(self):
        if self is not None:
            atual = self.primeiro
            self.primeiro = atual.primeiro.proximo
            atual.primeiro.proximo = None
            if self.__tamanho == 1:
                self.ultimo = None
        else:
            print("Lista vazia!")

        self.__tamanho -= 1
        self.__ite = None
