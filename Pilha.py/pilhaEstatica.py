class Pilha:
    """
    Pilha estatica
    """
    
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity

        # inicializa a pilha com o tamanho desejado
        self.pilha = [None] * capacity

    def push(self, data):
        """
        Adiciona um elemento no topo da pilha
        """
        
        if self.capacity == self.top + 1:
            print("Estouro de pilha")
            return
        
        self.top = self.top + 1
        self.pilha[self.top] = data

    def pop(self):
        """
        Retorna e remove o elemento do topo da pilha
        """
        
        if self.top == -1:
            print("Pilha vazia")
            return
    
        temp = self.pilha[self.top]
        self.top = self.top - 1

        return temp
    
    def size(self):
        """
        Retorna a quantidade de elementos da pilha
        """
        
        return self.top+1

    def isEmpty(self):
        """
        Retorna True se a pilha esta vazia
        """
        
        return self.top == -1

    def isFull(self):
        """
        Retorna True se a pilha esta cheia
        """
        
        return self.capacity == self.top + 1

    def getTop(self):
        """
        Retorna o topo da pilha sem remover
        """

        if self.isEmpty():
            print("Pilha vazia")
            return None

        return self.pilha[self.top]
    
    def clear(self):
        """
        Limpa a pilha
        """
        
        self.top = -1
        


    def __str__(self):
        """
        Retorna uma string com as informacoes da pilha
        quando o objeto e chamado dentro de um print() 
        ou dentro de um str(). 
        """
        
        # cria uma nova pilha auxiliar
        auxPilha = Pilha(self.capacity)
        
        # retira os elementos da pilha antiga e preenche a auxiliar
        # com isso, a auxiliar sera preenchida em ordem reversa
        for i in range( self.top+1 ):
            auxPilha.push( self.pop() )
            
        # cria uma string com os elementos da pilha auxiliar e
        # enquanto isso, preenche novamente a pilha original
        strPilha = '['
        for i in range( auxPilha.top+1 ):
            
            top = auxPilha.pop()
            
            # preenche a pilha original
            self.push(top)
            
            # guarda o top em uma string
            strPilha += ' ' + str(top)
            
        strPilha += ' ]'
        
        return strPilha
            
            
            


# testando a pilha
pilha = Pilha(10)

pilha.push(5)
print(pilha)

pilha.push(3)
print(pilha)

pilha.push(9)
print(pilha)

print( 'Size: ', pilha.size() )

valor = pilha.pop()
print(pilha)

valor = pilha.pop()
print(pilha)

print( 'Vazia?: ', pilha.isEmpty() )

valor = pilha.pop()
print(pilha)

print( 'Vazia?: ', pilha.isEmpty() )

valor = pilha.pop()
print(pilha)

pilha.push(2)
print(pilha)

pilha.push(14)
print(pilha)

print( 'Vazia?: ', pilha.isEmpty() )

pilha.clear()
print( 'Vazia?: ', pilha.isEmpty() )


