class Node:
    
    def __init__(self, data, next=None):
        
        self.data = data
        self.next = next
        
class Fila:
    """
    Fila dinâmica
    """
    
    def __init__(self, data = None):
        
        self.front = None
        self.rear = None
        self.size = 0
        
        if data is not None:
            self.enqueue(data)
            
    def isEmpty(self):
        
        if self.size == 0:
            return True
        else:
            return False
        
    def enqueueRear(self,valor):
        """
        Insere um elemento no final da fila
        """
        
        noh = Node( valor )
        
        if self.size==0:
            self.front = noh
            self.rear = noh
        
        else:
            self.rear.next = noh
            self.rear = noh
         
        # aumenta a qtd. de elementos da fila
        self.size += 1 
        
    def enqueueFront(self,valor):
        """
        Insere um elemento no inicio da fila
        """
        
        # cria um novo nó
        noh = Node(valor)
        
        if self.isEmpty():
            self.front = noh
            self.rear = noh
            
        else:
            
            noh.next = self.front
            
            self.front = noh

        # aumenta a qtd. de elementos da fila            
        self.size += 1
            
        
    def dequeueFront(self):
        """
        Elimina o primeiro elemento
        """
        
        if self.isEmpty():
            print('Erro. Underflow')
            return None
        else:
            
            nohAExcluir = self.front
            
            # retorna o valor
            valor = nohAExcluir.data
            
            # atualiza quem está na frente
            self.front = nohAExcluir.next
            
            # diminui o numero de elementos
            self.size -= 1
            
            # deleta o noh da memoria
            del nohAExcluir
            
            return valor
        
    def dequeueRear(self):
        """
        Elimina o ultimo elemento
        """
        
        if self.isEmpty():
            print('Erro. Underflow')
            return None
        else:
            
            nohAExcluir = self.rear
            
            # retorna o valor
            valor = nohAExcluir.data
            
            # atualiza quem esta atras. Precisa tambem atualizar o next do no que sera o novo rear.
            # o unico jeito de achar o noh que sera o novo rear, eh percorrendo toda a fila
            novoRear = self.front
            
            # percorre a fila ate achar o elemento anterior ao rear. 
            # o laco para quando achar o rear, isto eh, um next igual ao None.
            while novoRear.next is not None:
                novoRear = novoRear.next
                
            # troca o rear
            self.rear = novoRear
            
            # diminui o numero de elementos
            self.size -= 1

            # deleta o noh da memoria            
            del nohAExcluir
            
            return valor

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

    def getRear(self):
        """
        Retorna o ultimo elemento da lista sem remover
        """
        
        if self.rear is None:
            print("Pilha vazia")
            return None

        # iremos retornar apenas o dado do noh, mas
        # dependendo da necessidade, poderia ser
        # retornado o noh inteiro
        return self.rear.data
        
    def getSize(self):
        return self.size
    
    def __str__(self):
          
        # fila auxiliar para imprimir a fila original
        filaAux = Fila()
        
        # string que ira guardar os valores
        info = '[ '
        
        while not self.isEmpty():
            
            valor = self.dequeueFront()
            
            # insere na fila auxiliar
            filaAux.enqueueRear( valor )
            
            info = info + ' ' + str(valor)
        
        info = info + ' ]'
        
        # laço para recuperar a fila 
        while not filaAux.isEmpty():
            
            valor = filaAux.dequeueFront()
            self.enqueueRear(valor)
            
        return info
        
        
    
    
# testa a fila
fila = Fila()

fila.enqueueFront( 5 )
print('enqueueFront( 5 ): ', fila) 

fila.enqueueFront( 3 )
print('enqueueFront( 5 ): ', fila)

fila.enqueueFront( 9 )
print('enqueueFront( 9 ): ', fila)

fila.enqueueRear( 15 )
print('enqueueRear( 15 ): ', fila)      

res = fila.getSize( )
print('size( ): ', res, ' -- ', fila)   

res = fila.getFront( )
print('front( ): ', res, ' -- ', fila)   

res = fila.getRear( )
print('rear( ): ', res, ' -- ', fila)   

fila.dequeueFront( )
print('dequeueFront( ): ', fila)  

fila.dequeueRear( )
print('dequeueRear( ): ', fila) 

res = fila.isEmpty( )
print('isEmpty( ): ', res, ' -- ', fila)   
            
            
           
