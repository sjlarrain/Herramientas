#!/usr/bin/env python
# coding: utf-8

# In[1]:


def leer_path(path):
    with open(path) as file:
        lines=file.readlines()
        lines=[l.strip() for l in lines]
    return lines


# In[2]:


class Nodo:
    def __init__(self,posicion):
        self.posicion=posicion
        self.vecinos=[]
        self.paso=""
    
    def add_vecino(self,nodo):
        self.vecinos.append(nodo) #Representa un arco entre dos nodos
    
    def paso(self):
        self.paso="S"
        
    def __str__(self):
        return  'Nodo: {}'.format(self.posicion)

    


# In[3]:


def crear_grafo(matriz):
    nodos=dict()
    filas=len(matriz)
    columnas=len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            if matriz[i][j]=="O":
                if (i,j) not in nodos.keys():
                    nodo=Nodo((i,j))
                    nodos.update({(i,j):nodo}) #Crea elemento solo si existía
                for f, c in[(-1,0),(0,-1),(1,0),(0,1)]:
                    if i+f>=0 and j+c>=0 and i+f<filas and j+c<columnas: #bordes mapa
                        if matriz[i+f][j+c]=='O':
                            if (i+f, j+c) not in nodos.keys(): #Si no existe, lo agrego
                                vecino=Nodo((i+f,j+c))
                                nodos.update({(i+f,j+c):vecino})
                            else:
                                vecino=nodos[(i+f,j+c)]
                            nodos[(i,j)].add_vecino(vecino)
    return nodos
        


# In[4]:


i=0
def buscar_tigre(origen,destino):
    global nodos
    global recorrido
    global i
    inicio=nodos[origen]
    posicion=inicio
    mov=[]
    while posicion.posicion!=destino:
        i+=1
        print(i)
        for e in posicion.vecinos:
            if e.posicion==nodos[destino]:
                return mov 
            elif e.posicion!=destino:
                print("Legue")
                print(posicion)
                posicion=e
                if posicion.posicion not in recorrido:
                    recorrido.append(posicion.posicion)
                    print("entre")
                    recorrido.append(posicion)
                    buscar_tigre(posicion.posicion,destino)
                else:
                    break
            
                
    


# In[ ]:


matriz=leer_path("test.txt")
nodos=crear_grafo(matriz)
recorrido=[]
caza=buscar_tigre((5,5),(0,5))
print(caza)


# In[ ]:




