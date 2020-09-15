from l03 import graficar
import time
from itertools import chain
def problema_1a(lista):
    sol=[]
    for j in range(len(lista)):  #Se crea una lista vacia para poner los jueces
        l_left=lista[:j]
        l_right=lista[j+1:]
        ll=0
        lr=0
        for e in l_left:    #Se suman las listas para poder igualarlas posteriormente
            ll+=e
        for e in l_right:
            lr+=e
        if ll==lr:
            sol.append(j)    #Si la solucion esta, se suma
    return sol
            
            
'''Esta sería de notación n^2'''  

def problema_1b(lista):
    sol=[]               
    left=0
    lt=sum(lista)  #Se agrega left y la suma de la lista en general
    for i in range(len(lista)):
        juez=lista.pop(0)  #Se saca el juez
        lt-=juez #Se resta al juez de la suma anterior de la listas
        if left==lt:
            sol.append(i) #Se agrega si es equivalente
        left+=juez #Se agrega aal juez a la siguiente lista para continuar
        
    return sol

'''Esta sería de notacion n'''

def graf_a(lt,mult,nombre):
    datos=[]  
    tiempos=[]
    for e in range(1,mult,10):  #Se recorre una lista y se multiplica esa lista para mas datos  
        lt1=[lt]*e
        lt1=list(chain(*lt1))  #Se encadena para tener solo una lista
        start=time.time()
        funx=problema_1a(lt1)     
        end=time.time()
        tt=end-start
        datos.append(len(lt1)) #Se agrega la cantidad de datos
        tiempos.append(tt)     #Se agrega el tiempo
    graficar(datos,tiempos,nombre,"Q datos","tiempo")  #Se grafica los resultados

def graf_b(lt,mult,nombre):  #Exactamente la otra funcion
    datos=[]
    tiempos=[]
    for e in range(1,mult,10):
        lt1=[lt]*e
        lt1=list(chain(*lt1))
        x=len(lt1)
        start=time.time()
        funx=problema_1b(lt1)
        end=time.time()
        tt=end-start
        datos.append(x)
        tiempos.append(tt)
    graficar(datos,tiempos,nombre,"Q datos","tiempo")    


# # Pregunta 2



def problema_2(lista):
    min1=min(lista) # Primer minimo
    lista.pop(lista.index(min1)) #Lo saca
    min2=min(lista)#Segundo minimo
    lista.pop(lista.index(min2)) #Idem
    min3=min(lista)#Tercero minimo y no se quita por que no es necesario
    max1=max(lista)# Lo mismo con los dos primeros maximos
    lista.pop(lista.index(max1))
    max2=max(lista)
    resul1=[[min1,min2,min3],[min1,min2,max1],[min1,max1,max2],[min1,min2,max1]] #Lista con las combinaciones para entregar
    #posteiormente los factores
    resul=[min1*min2*min3,min1*min2*max1,min1*max1*max2,min1*min2*max1] #Multiplicaciones posibles
    nums=resul.index(min(resul))#Nota el menor resultado
    return resul1[nums]   #devuelve el menor resultado

#  # Pregunta 3


def verificador(palabra):#Funcion para dar vuelta la palabra y analizar si es palidromo
        t=""
        for e in palabra:
            t=e+t
        if palabra==t:
            return True
        return False

def finder(palabra): #Busca recursivamente los palidromos y al encontrarlos los adjunta a una lista global
    for i in range(2,len(palabra)-1):
        if verificador(palabra[i+1:]):
            x=palabra[i+1:]
            palab=palabra[:i+1]
            finder(palab)
            return outder.append(x)
            

def problema_3b(palabra): #Crea la lista global y luego busca recursivamente toda las palabras
    global outder
    outder=[]
    finder(palabra)
    return len(outder)#Entrega el largo de la lista
        
        



# # Pregunta 4




from copy import deepcopy as dc
def verificador(pal1,pal2): #Verefica que tengan todas las letras menos una. Lo contrario entrega un False
    j=0
    for i in range(len(pal1)):
        if pal1[i]==pal2[i]:
            continue
        if j==1:
            return False
        j+=1
    return True

def arbol(lista):#Crea un arbol con los cambios de las islas y luego al encontrar los cambios                
    islas=dict()#Los traspasa a un diccionario y lo retorna cuando tenga todas las combinaciones
    for e in lista:
        if e not in islas.keys():
            puentes=[]
            for f in lista:
                if e!=f and verificador(e,f):
                    puentes.append(f)
            islas.update({e:puentes})
    return islas

def solver(tree,inicio,fin,camino=[]): #Busca a traves de un Backtracking todos los caminos 
    if inicio==fin:
        p=dc(camino)
        ln=len(camino)
        solution.append(p)
    else:
        saltos=tree[inicio] #Inicia con la lista, si tiene posibilidad de avzar busca las posiblees opciones
        if len(saltos)>0:
            for e in saltos:
                c=dc(camino)
                if e not in c: #Si no ha visitado la lista toavia y es posible, la visita
                    c.append(e) #La agrega al camino
                    solver(tree,e,fin,c) #Busca nuevamente si no a llegado al fin
    
            
def problema_4(lista,inicio,fin): #Crea el arbol y la lista global para ir agregando los caminos posibles
    tree=arbol(lista)
    global solution
    solution=[]
    solver(tree,inicio,fin,[inicio])
    ln=100
    for e in solution:  #Retorna solo los caminos mas cortos
        if len(e)<ln:
            ln=len(e)
            exit=[e]
        elif len(e)==ln and e not in exit:
            exit.append(e)
    return exit
    



# # Pregunta 5


from copy import deepcopy as dc
class Punto:        #Creamos la clase punto donde tendra los valores de su posicion,valor y sus dos posibles vecinos
    def __init__(self,pos,valor):
        self.nombre=pos
        self.valor=valor
        self.sur=None
        self.este=None
    def add_sur(self,vecino):  #Agrega solo vecino si es que cumple las condiciones
        if (abs(self.valor-vecino.valor))<=1:
            self.sur=vecino
    def add_este(self,vecino):#Idem
        if (abs(self.valor-vecino.valor))<=1:
            self.este=vecino
    def __str__(self):
        return '[nombre{} valor:{} sur:{} este:{}]'.format(self.nombre,self.valor,self.sur,self.este)

def mapear(matriz):  #Crea un grafo con todo los objetos y sus vecinos si es que existen. 
    places=dict()  #Se van agregando al diccionario
    for row in range(len(matriz)):
        for col in range(len(matriz[0])):  #Recorremos la matriz
            dot=Punto((row,col),matriz[row][col])
            if (row,col) not in places.keys():
                places.update({(row,col):dot})
            if row+1<len(matriz):    #Si esta dentro de los limites lo busca y agrega
                if (row+1,col) not in places.keys():
                    este=Punto((row+1,col),matriz[row+1][col])
                    places.update({(row+1,col):este})
                else:
                    este=places[(row+1,col)]#Lo define como el este
            else:
                este=None
            if este!=None:
                places[(row,col)].add_este(este) #Si el este existe lo agrega al objeto
            if col+1<len(matriz[0]): #Lo mismo con las columnas y lo agrega al final
                if (row,col+1) not in places.keys():
                    sur=Punto((row,col+1),matriz[row][col+1])
                    places.update({(row,col+1):sur})
                else:
                    sur=places[(row,col+1)]
            else:
                sur=None    
            if sur!=None:
                places[(row,col)].add_sur(sur)
    return places
    

def continuar(objeto,camino=[]):#Toma el objeto y lo busca recursivamente avanzando entre sus atributos
    e=dc(camino)
    s=dc(camino)
    if objeto.este!=None: #Como sabemos pueden tener mas de un camino
        e.append(objeto.valor)
        continuar(objeto.este,e)
    if objeto.sur!=None:
        s.append(objeto.valor)
        continuar(objeto.sur,s)
    resultados.append(e)#Al no poder avanzar en ninguno de los caminos agrega los caminos ya encontrados
    resultados.append(s)
    
def problema_5(matriz):
    global resultados
    resultados=[]
    sujetos=mapear(matriz)#Crea el diccionario y las listas globales exigidas
    for e in sujetos.values(): #Busca los caminos para cada objeto que le dimos
        continuar(e)
    ln=0
    exit=[]
    for e in resultados: #Devuelve solo las listas mas largas
        if len(e)>ln:
            ln=len(e)
            exit=[e]
        elif len(e)==ln and e not in exit:
            exit.append(e)
    return exit




