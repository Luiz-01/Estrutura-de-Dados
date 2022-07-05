class Node:
    """
    Noh de uma fila dinamica
    """
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class Fila:
    """
    Fila dinamica
    """

    def __init__(self, data  = None):
        self.front = None
        self.rear = None
        self.size = 0
        
        # se na criacao da fila, um dado ja for passado
        # usa a funcao enqueue para adicionar esse dado
        if data is not None:
            self.enqueue(data)

    def enqueue(self, data):
        """
        Adiciona um elemento no final da fila
        """

        # cria um novo noh com o dado informado, mas que 
        # nao aponta para nenhum outro, ja que sera o ultimo da fila
        tempNode = Node(data)
            
        # se a fila esta vazia, o element rear
        # ira receber o novo noh.
        # Nesse caso,o elemento front devera apontar para 
        # o mesmo noh do elemento rear
        if self.rear is None:
            self.rear = tempNode
            self.front = self.rear
            
        else:
            
            # o noh rear sera substituido pelo novo noh e, por isso,
            # deve apontar para o novo noh
            self.rear.next = tempNode
            
            # o noh rear aponta para o novo noh
            self.rear = tempNode
        
        self.size += 1

    def dequeue(self):
        """
        Retorna e remove o elemento no inicio da fila
        """
        
        if self.size == 0:
            print("Fila vazia")
            return None
        
        # pega o dado do elemento front atual
        data = self.front.data
        
        # o novo elemento front sera o noh que o 
        # elemento front que esta sendo removido estava apontando antes
        self.front = self.front.next
        
        # caso o novo elemento front seja None (ou seja, a fila ficou vazia) 
        # o elemento rear tambem deve ser setado como none
        if self.front is None:
            self.rear = None
        
        # diminui a quantidade de elementos da fila
        self.size -= 1

        # iremos retornar apenas o dado do noh, mas
        # dependendo da necessidade, poderia ser
        # retornado o noh inteiro
        return data
    
    def getSize(self):
        """
        Retorna a quantidade de elementos da fila
        """
        
        return self.size

    def isEmpty(self):
        """
        Retorna True se a fila esta vazia
        """
        
        return self.front is None

    def getFront(self):
        """
        Retorna o primeiro elemento da lista sem remover
        """
        
        if self.front is None:
            print("Pilha vazia")
            return None

        # iremos retornar apenas o dado do noh, mas
        # dependendo da necessidade, poderia ser
        # retornado o noh inteiro
        return self.front.data

    def clear(self):
        """
        Limpa a fila
        """
        
        while not self.isEmpty():
            data = self.dequeue()
            
    def __str__(self):
        """
        Retorna uma string com as informacoes da fila
        quando o objeto e chamado dentro de um print() 
        ou dentro de um str(). 
        """

        # cria uma nova fila auxiliar
        auxfila = Fila()
        
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


 
