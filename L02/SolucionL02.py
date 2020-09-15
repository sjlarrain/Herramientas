#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#La funcion construida es iterativa que va podando las opciones a medida que va avanzado la interacion
#De esta forma se reduce las opciones que ya fueran revisadas. De igual forma se genera un set para colocar
#solo las opciones verdaderamente independientes y en modo tupla para que no puedan ser editadas.
#Se asume que los numeros son todos distintos 
def problema_1(lista,entero):            
    lista.sort()
    lista=lista[:entero-3]
    lt=set()
    c=0
    for i in lista:
        c+=1
        d=0
        for j in lista[c:]:
            d+=1
            if len({i,j})==2 and i+j<entero: 
                for k in lista[d:]:
                    if len({i,j,k})==3 and i+j+k<entero+1:
                        if (entero-i-j-k) in lista:
                            if len({i,j,k,(entero-i-j-k)})==4:
                                lt1=sorted([i,j,k,(entero-i-j-k)])
                                lt1=tuple(lt1)
                                lt.add(lt1)   
    return (len(lt),list(lt))
                    


# In[ ]:


get_ipython().run_cell_magic('time', '', 'lista=[2,7,4,0,9,5,1,3]\nlista=list(range(100))\nentero = 256\nprint(problema_1(lista,entero))')


# In[ ]:


#Este problema se toma la lista y despues se crean dos lista para guardar a cualquier nuevo jugador y para
#las jugadas de los individuos. Luego tenemos una interacion de la listas con las ordenes y un diccionario para contar
#las veces que han movido esa ficha y ese jugador. Por ultimo se retorna la lista de jugadas
def problema_2(lista): 
    jug=[]
    jugadas=[]
    dt=dict()
    for e in lista:
        if e[0] in jug:
            if e in dt:
                dt[e]+=1
            else:
                dt[e]=1  
        else:
            jug.append(e[0])
            jugadas.append(e[0]+": Ha realizado su primera jugada")
            dt[e]=1
        jugadas.append(e[1]+str(dt[e]))
           
    return jugadas
        


# In[ ]:


get_ipython().run_cell_magic('time', '', "lista=[('J1','alfil'),('J2','perro'),('J1','gato'),\n('J1','alfil'),('J3','alfil'),('J2','alfil'),('J1','alfil')]\nprint(problema_2(lista))")


# In[ ]:



def problema_3(lista):
    def keyOrd(x):
        return x.numero
    def convertidor(lista):#Primero se convierten todos los numeros hexadecimal a numeros decimales para poder trabajar mas facilmente con ellos
        lt=[]
        for e in lista:
            lt1=[]
            for f in e:
                f=int(f,16) 
                lt1.append(f)
            lt.append(lt1)
        return lt
    
    class Numero: #Crea los nodos necesarios
        def __init__(self,numero,lista):
            self.numero=numero
            self.suma= lista
            self.primos=""
        def add_primos(self,x): #Agrega los puntos de cambio
            self.primos=x
        def __str__(self):
            return str((self.numero,self.suma))
        def __repr__(self):
            return str((self.numero,self.suma))
            
    def primos(num,listas): #Ve donde se puede cambiar y por eso se llama primo.
        prim=[]
        for e in listas:
            for f in e:
                if num.numero==f.numero and num.suma!=f.suma:
                    prim.append((f,e[f.numero+1:]))
        return prim
        
    lt_num=[]        
    lista2=convertidor(lista)
    for e in lista2:
        numbers=[]
        for f in range(len(e)):
            num=Numero(int(e[f]),sum(e[f+1:]))
            numbers.append(num)
        lt_num.append(numbers)
    for e in lt_num:
        for f in e:
            pris=primos(f,lt_num)
            f.add_primos(pris)
    print (lt_num)
            
    


# In[ ]:


get_ipython().run_cell_magic('time', '', "lista=[['0', '1', '3', '5', '7', '8', 'a'],\n['0', '1', '9', 'a', 'b', 'c', 'e', 'f'],\n['2', '3', '4', '6', '7', '9', 'c']]\n\nprint(problema_3(lista))")


# In[ ]:


#Se crea un grafo que se baso en la actividad dos y la clase letra con sus adyacentes u su posicion en la matriz.
#En el grafo se analiza una letra y se colocan todos los letras adyacentes ya que uno puede construir las palabras 
#En cualquier direccion. Por ultimo la funcion buscar palabra busca la primera letra de la palabra buscada. Esto 
#Se hace para buscar solo las palabras necesarias.
#Si fue encontrada la palabra utilizamos la construir para ver si se logra la realizacion de la palabra buscada. Solo 
#Si el resultado encontrado es identico a la palabra buscada la retornara. De lo contrario no retornara nada (None)
#Luego se construye un set en caso de que la palabras esten repitidas. Solo retorna las palabras encontradas
def problema_4(lista1,lista2):
    class Letra:
        def __init__(self,let):
            self.let=let
            self.pos=""
            self.ady=[]
        def add_ady(self,letra):
            self.ady.append(letra)
        def add_pos(self,tup):
            self.pos=tup
        def __str__(self):
            return self.let
        
    def crear_grafo(lista2):        #La construccion de esta funcion se baso en la de la actividad 2
        grafo=dict()   #Diccionario para construir el grafo. Nos permite ver las letras y la tupla incorporada
        filas=len(lista2) #Demarcamos el tamaño de la matriz
        columnas=len(lista2[0])
        for e in range(filas): #Recorremos para irconstruyendo el grafo
            for f in range(columnas):
                if (e,f) not in grafo.keys(): #De no estar en el diccionario significa que no a sido construido. APlicamos clase
                    letras=Letra(lista2[e][f])
                    letras.add_pos((e,f))
                    grafo.update({(e,f):letras})
                for i, j in[(-1,0),(0,-1),(1,0),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]: #Analizamos a todos sus adyacentes en toda
                    if i+e>=0 and j+f>=0 and i+e<filas and j+f<columnas: #direccion y vemos si esta en la matriz
                        if (i+e, j+f) not in grafo.keys(): #De existir y no haber sido construido aplicamos cosntruccion
                            ady=Letra(lista2[i+e][j+f])
                            ady.add_pos((i+e,j+f))
                            grafo.update({(i+e,j+f):ady})
                        else:
                            ady=grafo[(i+e,j+f)]
                        grafo[(e,f)].add_ady(ady) #Por ultimo lo agregamos a los adyacentes de la posicion recorrida
        return grafo
    
    def construir(objeto, palabra,resul,n):  #Construye la palabra y si logra construirla de forma recursiva. 
        for r in objeto.ady:                #De lo cntrario no retorna nada. Solo devolvera si n es igual al largo de la palabra
            if n==len(palabra):
                return resul
            elif r.let==palabra[n]:
                resul+=r.let
                sg=construir(r,palabra,resul,n+1) 
                return sg
    
    def buscar_palabra(palabra,grafo): #Busca la primera letra en el grafo para asi encontrar la posicon donde empezar
        for e in range (len(lista2)): #a buscar recursivamente con construir
            for f in range(len(lista2[0])):
                dic=grafo[(e,f)]
                if dic.let==palabra[0]:
                    return[dic,dic.let]
    
    grafo=crear_grafo(lista2) 
    encontradas=set()
    for e in lista1:
        pal=buscar_palabra(e,grafo) #Busca la letra, si lo hace, sigue buscando recursivamente, de lo contrario
        if pal:          #Pasa a la siguiente
            pal1=construir(pal[0],e,pal[1],1)
        if pal1: encontradas.add(pal1)
    return encontradas
        


# In[ ]:


get_ipython().run_cell_magic('time', '', "palabras=['ARBOL','CASA','PAR','EL','PERRO','TANGO','RAR0','FUTBOL','PASA','LUPE','CLARO','ARO','BLORA','CLB','BLC']\nletras=[['A','S','A','P'],['A','R','O','E'],['C','L','B','Q']]\nprint(problema_4(palabras,letras))")


# In[ ]:


#En este problema primero ordenamos la lista por edad para poder incorporar los individuos y encontrar el nodo raiz.
#Asumimos que el padre siempre tendrá que ser mayor que sus hijos. Se construyen todos los indivuduos de acuerdo
#A lo aprendido en las clases del material entregado. Se agrega el atributo "level" al arbol para poder diferenciar
#El nivel que el individuo se encuentra, para poder identificar la cantidad de individuos contagiados por nivel
def problema_5_1(lista):
    def keyOrd(lista):
        return lista[1]
    
    class Arbol:
        
        def __init__(self,nombre,edad,portador,padre,c): #Crea al individuo
            self.nombre=nombre
            self.edad=edad
            self.portador=portador
            self.padre=padre
            self.hijos=[]
            self.level=c
        
        def add_hijo(self,indv): #Agrega a los hijos. Todo hijo debe tener un padre relacionado con la raiz.
            if self.nombre==indv[3]: #Si encuentra a su padre lo agregará.Lo agrega si el nombre del encontrado es  
                c=Arbol(indv[0],indv[1],indv[2],indv[3],self.level+1)#identico al que esta en el factor entrregado
                self.hijos.append(c)
            else:
                for hijos in self.hijos: #Si no a encontrado al padre sigue buscando en los hijos de ese individuo
                    hijos.add_hijo(indv) #de forma recursiva
        def __repr__(self):
            def im_hijos(nodo):
                for e in nodo.hijos:
                    self.ret+="Nombre: {} Edad: {} Portador: {} Padre: {} Level:{} \n".format(e.nombre, e.edad, e.portador, e.padre,e.level)
                    im_hijos(e)
                return self
            self.ret="RAIZ ->Nombre: {} Edad: {} Portador: {} Level: {}\n".format(self.nombre, self.edad, self.portador, self.level)
            im_hijos(self)
            return self.ret
    
    lista.sort(key=keyOrd,reverse=True)
    T=Arbol(lista[0][0],lista[0][1],lista[0][2],lista[0][3],0)
    for e in lista[1:]:
        T.add_hijo(e)
    return T


# In[ ]:


#Esta funcion recibe la lista, la ordena y luego crea a los individuos. Para crear a los individuos busca al padre en
#Un diccionario, de esta forma sabe a que nivel se encuentra.Tambien lo agrega a una lista donde estan todos los miembros
#De la familia posterior a eso aplicamos la funcion nivel que busca 
#Cual es el nivel que tiene la mayor cantidad de contagiados y le retorna los nombres, el nivel en que esta y la cantidad.
def problema_5_3(lista):
    def keyOrd(lista): #Permite el ordenamiento por edad. Asumimos que el padre siempre será mayor.
        return lista[1]
    def nivel(lista): # Busca el nivel con mas contagiados. Indviduos es el diccionario con el nivel de contagiados
        indv=dict()
        for e in lista:#Revisa los contagiadospor nivel
            if e.level in indv.keys() and e.portador:
                indv[e.level]+=1
            elif e.level not in indv.keys() and e.portador:
                indv[e.level]=1
        c=0
        for e in indv.items():#Devuelve el mayor nivel contagiado
            if list(e)[1]>c:
                c=list(e)[1]
                x=list(e)[0]
        cont=[]
        for e in lista: #Devuelve los contagiados 
            if e.level==x and e.portador:
                cont.append(e.nombre)
        return (len(cont),cont)
    class Persona:
        def __init__(self,nombre,edad,portador,padre,c): #Crea al individuo
            self.nombre=nombre
            self.edad=edad
            self.portador=portador
            self.padre=padre
            self.hijos=[]
            self.level=c
    
    lista.sort(key=keyOrd, reverse=True)
    arbol=dict()#Da los padres y su nivel para luego asignarle el nivel al hijo
    tree=[] #Lista de los individuos
    raiz=Persona(lista[0][0],lista[0][1],lista[0][2],lista[0][3],0)
    arbol.update({raiz.nombre: 0})
    tree.append(raiz)
    for e in lista:#Crea a todos los individuos y les asigna nivel y los agrega a la lista
        if e[3] in arbol.keys():
            indv=Persona(e[0],e[1],e[2],e[3],arbol[e[3]]+1)
            arbol.update({indv.nombre:arbol[e[3]]+1})
            tree.append(indv)
    sald=nivel(tree)#Encuentra el nivel más contagiado
    return sald


# In[ ]:


from collections import deque
def problema_5_4(lista):
    pass
    def keyOrd(lista):
        return lista[1]
    class Persona:
        def __init__(self,nombre,edad,portador,padre,c): #Crea al individuo
            self.nombre=nombre
            self.edad=edad
            self.portador=portador
            self.padre=padre
            self.level=c
            self.hijos=[]
            
    
    lista.sort(key=keyOrd, reverse=True)
    arbol=dict()#Da los padres y su nivel para luego asignarle el nivel al hijo
    tree=[] #Lista de los individuos
    raiz=Persona(lista[0][0],lista[0][1],lista[0][2],lista[0][3],0)
    arbol.update({raiz.nombre: 0})
    tree.append(raiz)
    for e in lista:#Crea a todos los individuos y les asigna nivel y los agrega a la lista
        if e[3] in arbol.keys():
            indv=Persona(e[0],e[1],e[2],e[3],arbol[e[3]]+1)
            arbol.update({indv.nombre:arbol[e[3]]+1})
            tree.append(indv)
    sin_hijos=[]
    for e in tree: #Revisa a que nivel estan los jovenes y los agrega a una lista
        if len(e.hijos)==0:
            sin_hijos.append(e)
    niveles=set() #Revisa la lista y ve los niveles descritos
    for e in sin_hijos:
        niveles.add(e.level)
    
    niveles=list(niveles)
    niveles.sort
    resul=[]
    for e in range(len(niveles)):#Calcula la diferencia entre los niveles
        if e+1<len(niveles):
            re=niveles[e+1]-niveles[e]
            resul.append(re)
    c=False
    for e in resul: #Si en la lista de resultados hay una diferencia mayor a 1 significa que hay posibilidad de contagio
        if e>1:
            c=True
    return c
        
    
    


# In[ ]:


get_ipython().run_cell_magic('time', '', 'lista=[["Francisco", 99999, False, None],\n["Felipe", 53, True, "Francisco"],\n["Pablo", 34, True, "Felipe"],\n["Cristobal", 25, False, "Felipe"],\n[\'Santiago\',21,True,\'Felipe\'],\n[\'Francois\',20, True, \'Santiago\'],\n[\'Agustin\',20, True, \'Santiago\'],\n[\'Ramiro\',20, False, \'Santiago\'],\n[\'Martin\',20, True, \'Santiago\'],\n[\'Alejo\',20, True, \'Santiago\']]\nprint(problema_5_1(lista))\nprint(problema_5_3(lista))\nprint(problema_5_4(lista))')


# In[ ]:


get_ipython().run_cell_magic('time', '', "lista=[['Leonor Perla Mondragón', 53, True, 'Aurelio Isaac Sauceda'],\n ['Flavio Marisela Jaime Barrera', 53, False, 'Conchita Leticia Casanova Collado'],\n ['Delia Casanova', 116, True, None],\n ['Martha Miriam Guajardo', 8, True, 'Leonor Perla Mondragón'],\n ['Juan Cano', 103, False, 'Delia Casanova'],\n ['Angélica Catalina Valencia', 63, True, 'Aurelio Isaac Sauceda'],\n ['Mtro. Silvano Lara', 47, True, 'Conchita Leticia Casanova Collado'],\n ['Ing. Gonzalo Serrano', 110, False, 'Delia Casanova'],\n ['Lic. Alta  Gracia Castañeda', 76, True, 'Juan Cano'],\n ['Graciela Barraza', 78, False, 'Juan Cano'],\n ['Elsa Navarro Guerrero', 7, False, 'Leonor Perla Mondragón'],\n ['Gerónimo Alvaro Cardenas', 9, False, 'Angélica Catalina Valencia'],\n ['Ing. Andrés Baca', 38, False, 'Graciela Barraza'],\n ['Bernardo Collado Solís', 33, True, 'Graciela Barraza'],\n ['Pamela Anabel Sauceda Raya', 15, True, 'Angélica Catalina Valencia'],\n ['Aurelio Isaac Sauceda', 87, False, 'Ing. Gonzalo Serrano'],\n ['Jorge Alejandro Mesa', 23, False, 'Lic. Alta  Gracia Castañeda'],\n ['Sessa Alicia Carreón', 24, False, 'Lic. Alta  Gracia Castañeda'],\n ['Conchita Leticia Casanova Collado', 83, True, 'Ing. Gonzalo Serrano']]\n\nprint(problema_5_1(lista))\nprint(problema_5_3(lista))\nprint(problema_5_4(lista))")

