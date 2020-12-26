class Quicksort:

    def __init__(self, sequencia):
        self.sequencia = sequencia

    @property
    def sorted_sequencia(self):

        tamanho_sequencia = len(self.sequencia) -1 

        if tamanho_sequencia <= 1:
            raise Exception('Só posso ordenar sequências com mais de 1 elemento')
    
        self.__sort(0, tamanho_sequencia)

        return self.sequencia

    def __sort(self, start, end): 

        if start >= end:
            return
    
        pivo = self.__partition(start, end)

        self.__sort(start, pivo - 1)
        self.__sort(pivo + 1, end)

    def __partition(self, start, end):    
        
        i = start

        pivo = self.sequencia[end]

        for numero in range(start, (end)):

            elemento = self.sequencia[numero]

            if elemento <= pivo:
                self.__swap(self.sequencia.index(elemento), i)
                i += 1
            
        self.__swap(i, end)

        return i


    def __swap(self, position_x, position_y):
        
        valor_x = self.sequencia[position_x]

        valor_y = self.sequencia[position_y]

        self.sequencia[position_x] = valor_y

        self.sequencia[position_y] = valor_x

