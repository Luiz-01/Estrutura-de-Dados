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
        
        # lista de adjacencia 
        self.adjList = []
        
    def addVertex(self,data):
        """
        Adicionar um vertice no grafo
        """
        
        # criando um novo vertice
        vertex = Vertex(data)
        
        # adiciona na lista de vertices
        self.verticesList.append(vertex)
    
        # adicionar uma lista na lista de adjacencias
        self.adjList.append( [] )
        
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
                
        # adiciona o vertice na lista de adjacencia
        # do vertice de origem
        destVertex = self.verticesList[idxDest]
        self.adjList[idxOrig].append(destVertex)
        
        # se o grafo nao e orientado, adiciona o vertice de origem como adjacente ao vertice de destino
        if self.directed==False:
            origVertex = self.verticesList[idxOrig]
            self.adjList[idxDest].append(origVertex)
        
        
        
        
    
    def __str__(self):
        
        info = '\nLista de adjacencias: \n'
        
        for idx, vertex in enumerate(self.verticesList):
            info += '\n' + str( vertex.data ) + ': ' 
    
            listaAdjacentes = self.adjList[ idx ]
            for idxAdj, vertexAdj in enumerate(listaAdjacentes):
                info += str(vertexAdj.data) + ' '
            
        return info
    
    
# testando o grafo
grafo = Graph()  

# adiciona vertices
grafo.addVertex(6)
grafo.addVertex(5)
grafo.addVertex(4)
grafo.addVertex(3)
grafo.addVertex(2)
grafo.addVertex(1)

# adiciona as arestas
grafo.addEdge(6,4)
grafo.addEdge(4,3)
grafo.addEdge(3,2)
grafo.addEdge(2,1)
grafo.addEdge(1,5)
grafo.addEdge(5,4)
grafo.addEdge(5,2)

print(grafo)
    
    