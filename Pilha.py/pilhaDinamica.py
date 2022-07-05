class Node:
    """
    Noh de uma pilha dinamica
    """
    
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class Pilha:
    """
    Pilha dinamica
    """
    
    def __init__(self, data  = None):
        self.head = None
        self.tamanho = 0
        
        if data is not None:
            self.push(data)

    def push(self, data):
        """
        Adiciona um elemento no topo da pilha
        """
        
        # se a pilha esta vazia, o element head
        # ira receber o novo noh. Mas, ele ira apontar
        # para None, pois nao existia nenhum noh antes
        if self.head is None:
            self.head = Node(data)
            
        else:
            
            # Cria um novo noh com o dado informado e que sera usado como novo topo. 
            # Esse novo noh ira apontar para o noh que era o topo antes
            temp = Node(data, self.head)
            
            # substitui o topo pelo novo noh
            self.head = temp
        
        self.tamanho += 1

    def pop(self):
        """
        Retorna e remove o elemento do topo da pilha
        """
        
        if self.head is None:
            print("Pilha vazia")
            return None
        
        data = self.head.data
        self.head = self.head.next
        
        self.tamanho -= 1

        # iremos retornar apenas o dado do noh, mas
        # dependendo da necessidade, poderia ser
        # retornado o no inteiro
        return data
    
    def size(self):
        """
        Retorna a quantidade de elementos da pilha
        """
        
        return self.tamanho

    def isEmpty(self):
        """
        Retorna True se a pilha esta vazia
        """
        
        return self.head is None

    def getTop(self):
        """
        Retorna o topo da pilha sem remover
        """
        
        if self.head is None:
            print("Pilha vazia")
            return None

        # iremos retornar apenas o dado do noh, mas
        # dependendo da necessidade, poderia ser
        # retornado o no inteiro
        return self.head.data
            
    def clear(self):
        """
        Limpa a pilha
        """
        
        while not self.isEmpty():
            data = self.pop()
            
    def __str__(self):
        """
        Retorna uma string com as informacoes da pilha
        quando o objeto e chamado dentro de um print() 
        ou dentro de um str(). 
        """
        # cria uma nova pilha auxiliar
        auxPilha = Pilha()
        
        # retira os elementos da pilha antiga e preenche a auxiliar
        # com isso, a auxiliar sera preenchida em ordem reversa
        while not self.isEmpty():
            data = self.pop()
            auxPilha.push( data )
            
            
            
        # cria uma string com os elementos da pilha auxiliar e
        # enquanto isso, preenche novamente a pilha original
        strPilha = '['
        while not auxPilha.isEmpty():
            
            top = auxPilha.pop()
            
            # preenche a pilha original
            self.push(top)
            
            # guarda o top em uma string
            strPilha += ' ' + str(top)
            
        strPilha += ' ]'
        
        return strPilha    
        




# testando a pilha
pilha = Pilha()

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


 
