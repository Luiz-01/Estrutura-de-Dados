class Node:
    
    def __init__(self, data):
        
        self.data = data
        self.right = None
        self.left = None
        
class Tree:
    """
    Arvore binaria de busca - implementacao dinamica
    """

    def __init__(self):
        self.root = None
        
    def insert(self, data, node = None):
        """
        Insere um novo noh. Considera a regra de arvores
        binarias de busca em que a subarvore esquerda de um determinado noh 
        deve ter uma chaves menores que a desse noh, enquanto que a subarvore direita 
        deve ter chaves maiores
        """
        
        # se a arvore ainda nao possui noh raiz
        if self.root == None:
            self.root = Node(data)
            
        else:
            
            if node is None: 
                node = self.root
        
            # se o valor do novo noh for menor que o valor do noh atual, insere na esquerda
            if data < node.data:
                
                if node.left is None:
                    
                    # insere um novo noh com o valor desejado na esquerda
                    node.left = Node(data)
                    
                else:
                    # se ja existe um noh na esquerda, nao podemos inserir o novo noh
                    # diretamente. Precisamos chamar a funcao insert recursivamente no 
                    # noh da esquerda
                    self.insert( data, node.left )
                
                
            # se o valor do novo noh for maior ou igual que o valor do noh atual, insere na direita
            else:
                
                if node.right is None:
                    
                    # insere um novo noh com o valor desejado na direita
                    node.right = Node(data)
                    
                else:
                    # se ja existe um noh na direita, nao podemos inserir o novo noh
                    # diretamente. Precisamos chamar a funcao insert recursivamente no 
                    # noh da direita
                    self.insert( data, node.right )           
             
    def strInorder(self, node = -1, info = ''):
        """
        Retorna uma string com os valores da arvore obtidos apos 
        o percurso "Em Ordem"
        """
        
        if self.root is None:
            return ' '
            
        else:
            
            if node==-1:
                node = tree.root
            
            if node.data is not None:
                
                if node.left is not None: 
                    info += self.strInorder(node.left)
                    
                info += ' ' + str(node.data) #print(data)
                
                if node.right is not None:
                    info += self.strInorder(node.right)
                    
                return info
            else:
                return info
            
            
    def strPreorder(self, node = -1, info = ''):
        """
        Retorna uma string com os valores da arvore obtidos apos 
        o percurso "Pre Ordem"
        """
        
        if self.root is None:
            return ' '
            
        else:
            
            if node==-1:
                node = tree.root
            
            if node.data is not None:
                
                info += ' ' + str(node.data)
                
                if node.left is not None: 
                    info += self.strPreorder(node.left)
                
                if node.right is not None:
                    info += self.strPreorder(node.right)
                    
                return info
            else:
                return info
            
    def strPostorder(self, node = -1, info = ''):
        """
        Retorna uma string com os valores da arvore obtidos apos 
        o percurso "Pre Ordem"
        """
        
        if self.root is None:
            return ' '
            
        else:
            
            if node==-1:
                node = tree.root
            
            if node.data is not None:
                              
                if node.left is not None: 
                    info += self.strPostorder(node.left)
                
                if node.right is not None:
                    info += self.strPostorder(node.right)
                    
                info += ' ' + str(node.data)
                    
                return info
            else:
                return info
            
        
    def buscar(self, searchedData, node = -1):
    
        if node == -1:
            node = tree.root
            
        if node.data is not None:
            
            if searchedData == node.data:
                return True
            
            elif searchedData < node.data:
                
                if node.left is not None: 
                    return self.buscar( searchedData, node.left )
                else: 
                    return False
            else:
                if node.right is not None:
                    return self.buscar( searchedData, node.right )
                else:
                    False
        else:
            return False 


#---------------------    
# testando a arvore

tree = Tree()
tree.insert(17)
tree.insert(6)
tree.insert(35)
tree.insert(4)
tree.insert(14)
tree.insert(23)
tree.insert(48)

info = tree.strInorder()
print('strInorder():', info)

info = tree.strPreorder()
print('strPreorder():', info)

info = tree.strPostorder()
print('strPostorder():', info)
        
res = tree.buscar(18)
print('buscar(18): ', res)
    
res = tree.buscar(23)
print('buscar(23): ', res)    
