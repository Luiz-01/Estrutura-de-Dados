class Node:
    """
    Noh para uma arvore AVL
    """
    
    def __init__(self, data):
        
        self.data = data
        self.right = None
        self.left = None

        # altura do noh. Usado para calcular o balanceamento da arvore
        self.height = 1 
        
class AVLTree:
    """
    Arvore AVL - implementacao dinamica
    """

    def __init__(self):
        self.root = None
        
    def insert(self, data, node = None):
        """
        Insere um novo noh. Considera a regra de arvores
        binarias de busca em que a subarvore esquerda de um determinado noh 
        deve ter uma chaves menores que a desse noh, enquanto que a subarvore direita 
        deve ter chaves maiores.
        Alem disso, como essa arvore eh AVL, a cada insercao, 
        caso a arvore fique desbalanceada, deve ser feito o balanceamento.
        """

        # se a arvore ainda nao possui noh raiz
        if self.root == None:
            self.root = Node(data)
            node = self.root
            return node
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
                    node.left = self.insert( data, node.left )
                
                
            # se o valor do novo noh for maior ou igual que o valor do noh atual, insere na direita
            else:
                
                if node.right is None:
                    
                    # insere um novo noh com o valor desejado na direita
                    node.right = Node(data)
                    
                else:

                    # se ja existe um noh na direita, nao podemos inserir o novo noh
                    # diretamente. Precisamos chamar a funcao insert recursivamente no 
                    # noh da direita
                    node.right = self.insert( data, node.right )  
                    
                    
            # atualiza a altura do noh
            node.height = 1 + self.getMax(self.getHeight(node.left),self.getHeight(node.right))
            
            balance = self.getBalance(node)
            
            # faz o balanceamento, caso seja necessario
            if balance > 1 and data < node.left.data:
                return self.rightRotation(node)
            
            elif balance < -1 and data > node.right.data:
                return self.leftRotation(node)
                
            elif balance > 1 and data > node.left.data:
                return self.leftRightRotation(node)
            
            elif balance < -1 and data < root.right.data:
                return self.rightLeftRotation(node)
        
            # atualiza o noh raiz com as alteracoes
            self.root = node
            return node
        
    def delete(self, data, node = -1):
        """
        Deleta o noh que possui valor igual ao que foi informado na entrada.
        """
        
        # verifica se eh a primeira iteracao da funcao recursiva
        if node == -1: 
            node = self.root
         
        # se o noh atual eh none, significa que a arvore ja foi percorrida. Por isso,
        # podemos usar o return para retornar e finalizar a recursao
        if node is None:
            return node
               
        # se o valor a ser removido eh menor que o valor do noh atual, procure na esquerda
        elif data < node.data:
            node.left = self.delete( data, node.left )
            
        # se o valor a ser removido eh maior que o valor do noh atual, procure na direita
        elif data > node.data:
            node.right = self.delete( data, node.right )
            
        # se o valor foi encontrado, remove o noh
        else:

            # se o filho da esquerda eh None, retorna o filho da direita para substituir o noh removido                       
            if node.left is None:
                tempNode = node.right
                
                # verifica se o noh que sera removido eh a raiz, pois em caso afirmativo, precisa atualizar
                if node == self.root:
                    self.root = tempNode
                
                node = None # remove o noh. Nao podemos usar "del node", pq a variavel node continuara sendo usada pela recursao
                return tempNode

            # se o filho da direita eh None, retorna o filho da esquerda para substituir o noh removido                       
            elif node.right is None:
                tempNode = node.left
                
                # verifica se o noh que sera removido eh a raiz, pois em caso afirmativo, precisa atualizar
                if node == self.root:
                    self.root = tempNode
                    
                node = None # remove o noh. Nao podemos usar "del node", pq a variavel node continuara sendo usada pela recursao
                return tempNode
                
            # se o noh a ser removido possui dois filhos
            else:
                                
                # procura o sucessor do noh que sera excluido
                # uma opcao de sucessor que poderia ser usada eh: o noh mais a direita da subarvore esquerda. Mas,
                # iremos usar como sucessor o noh mais a esquerda da subarvore a direita. 
                menorNoh = self.getMinNode(node.right)
                
                # altera o dado do sucessor 
                node.data = menorNoh.data
                
                # percorre o arvore ate o sucessor para remover, pois ele vai trocar de lugar com o dado excluido
                node.right = self.delete(menorNoh.data,node.right)
                
        if node is None:
            return node

        # atualiza a altura do noh
        node.height = 1 + self.getMax(self.getHeight(node.left),self.getHeight(node.right))
            
        balance = self.getBalance(node)
        
        # faz o balancealanceamento, caso seja necessario
        if balance > 1 and self.getBalance(node.left) >= 0:
            
            # chama a funcao que faz a rotacao a direita
            node = self.rightRotation(node)
            
            print('\nrightRotation')
            
        elif balance > 1 and self.getBalance(node.left) < 0:
            
            # chama a funcao que faz a rotacao esquerda-direita
            node = self.leftRightRotation(node)
            
            print('\nleftRightRotation')
        
        elif balance < -1 and self.getBalance(node.right) <= 0:
            
            # chama a funcao que faz a rotacao a esquerda
            node = self.leftRotation(node)
            
            print('\nleftRotation')
        
        elif balance < -1 and self.getBalance(node.right) > 0:
            
            # chama a funcao que faz a rotacao direita-esquerda
            node = self.rightLeftRotation(node)
            
            print('\rightLeftRotation')
        
        self.root = node
        return node

    def getMax(self, num1, num2):
        """
        Retorna o maximo entre dois numeros
        """        
        
        if num1>num2:
            return num1
        else:
            return num2
                
    def getMinNode(self, root):
        """
        Retorna o pai do menor noh e o menor noh
        """
        
        # se a raiz for None, retorna, pois nao existe nenhum noh filho para olhar
        if root is None: 
            return root

        # se o filho esquerdo do noh atual eh None, significa que ele eh folha e, portanto, o menor noh 
        elif root.left is None:
            return root
            
        # se nao entrou em nenhuma condicao anterior, significa que precisa continuar percorrendo o lado
        # esquerdo da arvore ate achar o menor noh
        else:
            return self.getMinNode(root.left)
        

    def leftRotation(self, root):
        """
        Rotacao a esquerda
        """
        
        newRoot = root.right
        root.right = newRoot.left
        newRoot.left = root

        # atualiza as alturas        
        root.height = 1 + self.getMax(self.getHeight(root.left),	 self.getHeight(root.right))
        
        newRoot.height = 1 + self.getMax(self.getHeight(newRoot.left), self.getHeight(newRoot.right))
        
        return newRoot
    
    def rightRotation(self, root):
        """
        Rotacao a direita
        """
        
        newRoot = root.left
        root.left = newRoot.right
        newRoot.right = root
        
        # atualiza as alturas
        root.height = 1 + max(self.getHeight(root.left),
						self.getHeight(root.right))
        
        newRoot.height = 1 + max(self.getHeight(newRoot.left),
						self.getHeight(newRoot.right))
        
        return newRoot
    
    def rightLeftRotation(self, root):
        """
        Rotacao direita-esquerda
        """

        root.right = self.rightRotation(root.right)
        return self.leftRotation(root)
        
    def leftRightRotation(self, root):
        """
        Rotacao esquerda-direita
        """
        
        root.left = self.leftRotation(root.left)
        return self.rightRotation(root)
        
    def getHeight(self, root):
        """
        Calcula a altura do noh
        """
        
        if not root:
            return 0
        
        return root.height
    
    def getBalance(self, node):
        """
        Calcula o fator de balanceamento do noh
        """
        
        if not node:
            return 0
        
        return self.getHeight(node.left) - self.getHeight(node.right)

    def strPreorder(self, node = -1, info = ''):
        """
        Retorna uma string com os valores da arvore obtidos apos 
        o percurso "Pre Ordem"
        """
        
        if self.root is None:
            return ''
            
        else:
            
            if node==-1:
                node = self.root
            
            if node.data is not None:
                
                info += '' + str(node.data)
                info += '('
                
                if node.left is not None: 
                    info += self.strPreorder(node.left)
                
                if node.right is not None:
                    info += self.strPreorder(node.right)
                    
                info += ')'
                return info
            else:
                return info


#---------------------    
# testando a arvore

tree = AVLTree()
tree.insert(17)
tree.insert(6)
tree.insert(35)
tree.insert(4)
tree.insert(14)
tree.insert(23)
tree.insert(48)

info = tree.strPreorder()
print('strPreorder():', info)

tree.delete(14)
print('delete(14):', tree.strPreorder())

tree.delete(4)
print('delete(4):', tree.strPreorder())

tree.delete(6)
print('delete(6):', tree.strPreorder())

tree.delete(48)
print('delete(48):', tree.strPreorder())

tree.delete(23)
print('delete(23):', tree.strPreorder())

tree.delete(35)
print('delete(35):', tree.strPreorder())

tree.delete(17)
print('delete(17):', tree.strPreorder())