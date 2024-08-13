class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class ListaVaziaException(Exception):
    pass

class ListaEncadeada:
    def __init__(self):
        self.head: Node | None = None
        self._quantidade = 0

    @property
    def vazia(self):
        return self._quantidade == 0

    @property
    def cheia(self):
        return False

    def __len__(self):
        return self._quantidade

    def _get_no_indice(self, posicao):
        if posicao < 0 or posicao >= len(self):
            raise IndexError("Posição fora dos limites da lista.")
        no = self.head
        for _ in range(posicao):
            no = no.proximo
        return no

    def get_antecessor(self, posicao):
        if posicao <= 0 or posicao > len(self):
            raise IndexError("Posição do antecessor fora dos limites.")
        return self._get_no_indice(posicao - 1)

    def inserir(self, posicao, valor):
        if posicao < 0:
            posicao = len(self) + posicao
        if posicao < 0:
            posicao = 0
        if posicao > len(self):
            posicao = len(self)

        novo = Node(valor)
        if posicao == 0:
            novo.proximo = self.head
            self.head = novo
        else:
            antecessor = self.get_antecessor(posicao)
            novo.proximo = antecessor.proximo
            antecessor.proximo = novo

        self._quantidade += 1

    def remover(self, posicao):
        if posicao < 0:
            posicao = len(self) + posicao
        if posicao < 0 or posicao >= len(self):
            raise IndexError("Posição fora dos limites da lista.")

        if self.vazia:
            raise ListaVaziaException("A lista está vazia.")

        if posicao == 0:
            self.head = self.head.proximo
        else:
            antecessor = self.get_antecessor(posicao)
            antecessor.proximo = antecessor.proximo.proximo

        self._quantidade -= 1

    def __str__(self):
        s = "["
        no = self.head
        while no is not None:
            s += repr(no.valor)
            no = no.proximo
            if no is not None:
                s += ", "
        s += "]"
        return s

    def obter(self, posicao):
        if posicao < 0:
            posicao = len(self) + posicao
        if posicao < 0 or posicao >= len(self):
            raise IndexError("Posição fora dos limites da lista.")
        no = self._get_no_indice(posicao)
        return no.valor

    def atribuir(self, posicao, valor):
        if posicao < 0:
            posicao = len(self) + posicao
        if posicao < 0 or posicao >= len(self):
            raise IndexError("Posição fora dos limites da lista.")
        no = self._get_no_indice(posicao)
        no.valor = valor

    @classmethod
    def intersecao(cls, lista1, lista2):
        resultado = cls()
        no1 = lista1.head
        while no1 is not None:
            no2 = lista2.head
            while no2 is not None:
                if no1.valor == no2.valor:
                    if resultado.vazia or not cls._existe(resultado, no1.valor):
                        resultado.inserir(len(resultado), no1.valor)
                    break
                no2 = no2.proximo
            no1 = no1.proximo
        return resultado

    @classmethod
    def uniao(cls, lista1, lista2):
        resultado = cls()

        no1 = lista1.head
        while no1 is not None:
            if resultado.vazia or not cls._existe(resultado, no1.valor):
                resultado.inserir(len(resultado), no1.valor)
            no1 = no1.proximo

        no2 = lista2.head
        while no2 is not None:
            if resultado.vazia or not cls._existe(resultado, no2.valor):
                resultado.inserir(len(resultado), no2.valor)
            no2 = no2.proximo

        return resultado

    @classmethod
    def diferenca(cls, lista1, lista2):
        resultado = cls()

        no1 = lista1.head
        while no1 is not None:
            if not cls._existe(lista2, no1.valor):
                resultado.inserir(len(resultado), no1.valor)
            no1 = no1.proximo

        return resultado

    @staticmethod
    def _existe(lista, valor):
        no = lista.head
        while no is not None:
            if no.valor == valor:
                return True
            no = no.proximo
        return False

# Testando os métodos

# Criando listas para teste
lista1 = ListaEncadeada()
lista1.inserir(0, 1)  # Inserção na posição 0
lista1.inserir(1, 2)  # Inserção na posição 1
lista1.inserir(2, 3)  # Inserção na posição 2

lista2 = ListaEncadeada()
lista2.inserir(0, 2)  # Inserção na posição 0
lista2.inserir(1, 3)  # Inserção na posição 1
lista2.inserir(2, 4)  # Inserção na posição 2

print("Lista 1:", lista1)
print("Lista 2:", lista2)

# Testando a interseção
resultado_intersecao = ListaEncadeada.intersecao(lista1, lista2)
print("Interseção:", resultado_intersecao)

# Testando a união
resultado_uniao = ListaEncadeada.uniao(lista1, lista2)
print("União:", resultado_uniao)

# Testando a diferença
resultado_diferenca = ListaEncadeada.diferenca(lista1, lista2)
print("Diferença (lista1 - lista2):", resultado_diferenca)
