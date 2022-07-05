class Fila:

    def __init__(self, capacity):

        self.capacity = capacity

        # inicializa a fila com o tamanho desejado
        self.queue = [None] * capacity
        
        # inicializa as posicoes do primeiro e ultimo 
        # elemento com -1
        self.front = -1
        self.rear = -1
        
        # no inicio, o tamanho da fila eh 0
        self.size = 0

    def enqueue(self, data):
        """
        Adiciona um elemento no final da fila
        """
        
        if self.size >= self.capacity:
            print("Estouro de fila")
            return
        
        else:
            
            # se for a primeira insercao na fila, precisa mudar os valores
            # das variaveis front e rear para 0
            if self.front==-1:
                self.front = 0
                self.rear = 0
            
            # se ultimo elemento da fila estiver no ultimo indice,
            # o novo elemento deve ser adicionado no indice 0.
            # Poderiamos evitar esse if se calculassemos o indice baseado
            # no resto da divisao de rear/capacity. Exemplo: se capacity
            # igual a 10 e rear igual a 9, (9+1)%10, daria 0. Se rear fosse
            # menor que 9, o (rear+1)%10 daria o proprio rear.
            elif self.rear==self.capacity-1:
                self.rear = 0
                
            else:
                self.rear = self.rear + 1
                
            # adiciona o elemento no final da fila
            self.queue[self.rear] = data
            
            # aumenta o tamanho
            self.size += 1

    def dequeue(self):
        """
        Retorna e remove o elemento no inicio da fila
        """
        
        if self.size == 0:
            print("Fila vazia")
            return None
        
        else:
    
            # retorna o primeiro elemento
            temp = self.queue[self.front]
            
            # se o tamanho for 1, quando remover, os indices 
            # front e rear devem virar -1
            if self.size == 1:
                self.front = -1
                self.rear = -1
            else:
                self.front = self.front + 1
            
            # diminui o tamanho
            self.size -= 1

        return temp
    
    def getSize(self):
        """
        Retorna a quantidade de elementos da fila
        """
        return self.size

    def isEmpty(self):
        """
        Retorna True se a fila esta vazia
        """
        return self.size == 0

    def isFull(self):
        """
        Retorna True se a fila esta cheia
        """
        return self.size == self.capacity

    def getFront(self):
        """
        Retorna o primeiro elemento da lista sem remover
        """
        
        if self.isEmpty():
            print("fila vazia")
            return None

        return self.queue[self.front]
    
    def clear(self):
        """
        Limpa a fila. Como o espaco para a fila ja esta 
        reservado, nao precisa efetivamente remover os valores.
        Basta alterar os indices e o valor size.
        """
        self.front = -1
        self.rear = -1
        self.size = 0
        


    def __str__(self):
        """
        Retorna uma string com as informacoes da fila
        quando o objeto e chamado dentro de um print() 
        ou dentro de um str(). 
        """
        
        # cria uma nova fila auxiliar
        auxfila = Fila(self.capacity)
        
        # retira os elementos da fila antiga e preenche a auxiliar
        for i in range( self.size ):
            auxfila.enqueue( self.dequeue() )
            
        # cria uma string com os elementos da fila auxiliar e
        # enquanto isso, preenche novamente a fila original
        strfila = '['
        for i in range( auxfila.size ):
            
            front = auxfila.dequeue()
            
            # preenche a fila original
            self.enqueue(front)
            
            # guarda o front em uma string
            strfila += ' ' + str(front)
            
        strfila += ' ]'
        
        return strfila
            
            
            


# testando a fila
fila = Fila(10)

fila.enqueue(5)
print(fila)

fila.enqueue(3)
print(fila)

fila.enqueue(9)
print(fila)

print( 'Size: ', fila.getSize() )

valor = fila.dequeue()
print(fila)

valor = fila.dequeue()
print(fila)

print( 'Vazia?: ', fila.isEmpty() )

valor = fila.dequeue()
print(fila)

print( 'Vazia?: ', fila.isEmpty() )

valor = fila.dequeue()
print(fila)

fila.enqueue(2)
print(fila)

fila.enqueue(14)
print(fila)

print( 'Vazia?: ', fila.isEmpty() )

fila.clear()
print( 'Vazia?: ', fila.isEmpty() )


