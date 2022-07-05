class Vertex:
    """
    Classe para cada vertice
    """
    
    def __init__(self,data):
        self.data = data
        
        
class Graph:
    """
    Cria um grafo por meio de lista
    de adjacencia
    """
    
    def __init__(self,directed=False):
        
        self.directed = directed
        
        # lista de vertices
        self.verticesList = []
        
        # matriz de adjacencia 
        self.adjMat = []
        
    def addVertex(self,data):
        """
        Adicionar um vertice no grafo
        """
        
        # criando um novo vertice
        vertex = Vertex(data)
        
        # adiciona na lista de vertices
        self.verticesList.append(vertex)
    
        # adiciona uma coluna de 0
        # em cada linha dos vertices que ja existem
        for idx in range( len(self.verticesList)-1):
            self.adjMat[idx].append(0)
            
        # criando uma nova linha 
        # para o novo vertice
        linha = [0]*( len(self.verticesList)+1 )
            
        # adicionar a linha na matriz
        self.adjMat.append( linha )
        
    def addEdge(self, orig, dest):
        """
        Adiciona uma aresta entre dois vertices
        """
        
        idxOrig = -1
        idxDest = -1
        for idx, vertex in enumerate(self.verticesList):
            
            if orig == vertex.data:
                idxOrig = idx
                
            if dest == vertex.data:
                idxDest = idx
                
        # adiciona 1 na matriz na posicao orig, dest
        self.adjMat[idxOrig][idxDest] = 1
        
        # se o grafo nao for direcionado
        # adiciona 1 na matriz na posicao dest, orig
        if self.directed==False:
            self.adjMat[idxDest][idxOrig] = 1
        
        
        
        
    
    def __str__(self):
        
        info = '\nMatrix de adjacencias: \n'

        # gera uma linha apresentando os vertices
        info += '   '
        for lin, vertex in enumerate(self.verticesList):
            info += str( vertex.data ) + ' '
        
        # gera uma linha pontilhada 
        info += '\n   ' + len(self.verticesList)*2*'-'
            
        for lin, vertex in enumerate(self.verticesList):
            info += '\n' + str( vertex.data ) + ' |'
             
            for col, vertex in enumerate( self.verticesList ):
                info += str(self.adjMat[lin][col]) + ' '
               
        return info
    
    
# testando o grafo
grafo = Graph()  

# adiciona vertices
grafo.addVertex(1)
grafo.addVertex(2)
grafo.addVertex(3)
grafo.addVertex(4)
grafo.addVertex(5)
grafo.addVertex(6)

# adiciona as arestas
grafo.addEdge(1,2)
grafo.addEdge(1,5)
grafo.addEdge(1,1)
grafo.addEdge(2,3)
grafo.addEdge(2,5)
grafo.addEdge(3,4)
grafo.addEdge(5,4)
grafo.addEdge(4,6)

print(grafo)
    
    