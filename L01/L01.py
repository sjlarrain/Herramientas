#!/usr/bin/env python
# coding: utf-8

# MENUS Y DICCIONARIOS

# In[1]:


#Listas
#Plataforma

#Proyectos
menuPest="El estado es:\n Planificacio[0]\n Ejecucion[1]\n Finalizado[2]"
menuPestd={0:"Planificacion",1:"Ejecucion",2:"Finalizado"}
menuPCimp="El impacto es:\n Local[0]\n Regional[1]\n Nacional[2]\n Global[3]"
menuPCimpd={0:"Local",1:"Regional",2:"Nacional",3:"Global"}


#Instituciones
menuIa="El estado de tipo:\n Público[0] \n Privada[1] \n Social[2]"
menuIe="El estado de tipo:\n Público[0] \n Privada[1]"
menuIad={0:"Público",1:"Privada",2:"Social"}
menuIt="Es de tipo:\n Economico[0]\n Tecnico[1]\n Gestion[2]\n "
menuItd={0:"Economico",1:"Tecnico",2:"Gestion"}

#Proyectos
menuPt="El proyecto es de tipo:\n Concientización[0] \n Ejecucion[1]"
menuPtd={0:"Concientización",1:"Ejecucion"}
menuPCi="El proyecto tiene impacto:\n Local[0]\n Regional[1]\n Nacional[2]\n Global[3]"
menuPCid={0:"Local",1:"Regional",2:"Nacional",3:"Global"}


#Filtros
menuFd={0:"Categoria",1:"Fecha"}

#Menu Editor
menuEp=("Editar:\n NOMBRE[0]\n DESCRIPCION[1]\n FECHA[2]\n ESTADO[3]\n JEFE[4]\n")
menuEpC=("Editar:\n TEMA[0]\n IMPACTO[1]\n CONTINUAR[2]")
menuEpE=("Editar:\n CIUDAD[0]\n COSTO[1]\n CONTINUAR[2]")
#Menu Eliminador
cargos={0:"jefe",1:"analista",2:"obrero",3:"institucion",4:"proyecto"}


# In[2]:


import datetime as dt
import random as rd
class Voluntario:
    def __init__(self,name,age,fecha):
        self.name=name
        self.age=age
        self.date=fecha
        self.accion=""
        self.proyectos=[]
    def __str__(self):
        t="Nombre: "+self.name+" Edad: "+str(self.age)+" Fecha entrada: "+str(self.date)+" Accion: "+self.accion
        return t
    
    def incluir_proyecto(self,proy):
        self.proyectos.append(proy)
        
    def incluir_jefe(self,jefe):
        self.jefes.append(jefe)
    
    def accionar(self,accion):
        self.accion=accion

class Jefe(Voluntario):
    cargo="jefe"
    def __init__(self,name,age,fecha):
        super().__init__(name,age,fecha)
    def __str__(self):
        t=super().__str__()+"\n"
        t+="Proyectos a cargo:\n"
        for e in self.proyectos:
            t+="   "+e.name+"\n"
        return t
        

class Analista(Voluntario):
    cargo="analista"
    def __init__(self,name,age,fecha,especialidad):
        super().__init__(name,age,fecha)
        self.especialidad=especialidad
        self.jefes=[]
        
    def __str__(self):
        t=super().__str__()+" Especialidad: "+self.especialidad+"\n"
        for i in range(len(self.jefes)):
            t+="Proyecto: "+self.proyectos[i].name+" Jefe:"+self.jefes[i].name+"\n"
        return t
            
class Obrero(Voluntario):
    cargo="obrero"
    def __init__(self,name,age,fecha):
        super().__init__(name,age,fecha)
        self.jefes=[]
    def __str__(self):
        t=super().__str__()+"\n"
        for i in range(len(self.jefes)):
            t+="Proyecto: "+self.proyectos[i].name+" Jefe:"+self.jefes[i].name+"\n"
        return t


# In[3]:



class Proyecto:               
    cargo="proyecto"
    tipo="Planificacion"                          #Clase Proyecto que incorpora todos los atributos utilizados por las
    def __init__(self,name,desc,fecha,estado):      #las sub clasescombinadas. Los metodos son para ambas sub clases
        self.name=name                              #Ejecucion y Concientizacion. Ademas se incorpora el metodo __str__ 
        self.desc=desc                              #para la impresion de ambos. Este último e init son ocupados en la
        self.date=str(fecha)                        #herencia de subclases
        self.est=estado
        self.jefe=Jefe("","","")
        self.analista=[]
        self.obrero=[]
        self.logs=[]
        self.instituciones=[]
        
    def __str__(self):
        t="Nombre: "+self.name+"\n"+" Descripcion: "+self.desc+"\n"
        t+="Jefe: "+self.jefe.name+"\n"
        t+=" Analistas:\n"
        for e in self.analista:
            t+=e.name+" \n"
        t+=" Obreros:\n"
        for e in self.obrero:
            t+=e.name+"\n"
        
        return t
    
        
    def imprimir_analista(self):                       #Los metodos son utilizados para la incorporacion y creacion de los
        print(self.analista)                           #proyectos
    def incluir_jefe(self,seleccion):
        self.jefe=seleccion
    def incluir_estado(self,estado):
        self.est=estado
    def incluir_analistas(self,lista):
        self.analista=lista
    def incluir_obrero(self,lista):
        self.obrero=lista
    def incluir_logs(self,accion):
        self.logs.append(accion)
    def incluir_instituciones(self,institucion):
        if len(self.instituciones)<2:
            self.instituciones.append(institucion)
        else:
            print("Ha superado el limite")

class Concientizacion(Proyecto):
    tipo="Concientizacion"
    def __init__(self,name,desc,fecha,tema,impacto,estado):
        super().__init__(name,desc,fecha,estado)
        self.tema=tema
        self.impacto=impacto
    def __str__(self):
        t=super().__str__()+" Tema: "+self.tema+"\n"+" Impacto: "+self.impacto+"\n "
        t+="\n "
        return t
         

class Ejecucion(Proyecto):
    tipo="Ejecucion"
    def __init__(self,name,desc,fecha,city,cost,estado):
        super().__init__(name,desc,fecha,estado)
        self.city=city
        self.cost=cost
    def __str__(self):
        t=super().__str__()+" Ciudad: "+self.city+"\n"+" Costo: $"+str(self.cost)+"\n"
        t+="\n "
        return t


# In[4]:


class Instituciones:
    cargo="institucion"
    def __init__(self,name,tipo,estado):
        self.name=name
        self.tipo=tipo
        self.estado=estado
    
    def __str__(self):
        t="Nombre:"+self.name+" Tipo:"+self.tipo+" Categoria:"+self.estado
        return t


# FUNCIONES

# In[5]:


#Funciones generales
safer=99999999999999999999
def val_num(tipo,num):       #Valida las entradas numeradasy las convierte en su forma int para su posterior uso bien 
    if tipo.isdigit():       #permite la incoporacion del verdadero producto. Tambien valida las opciones disponibles
        if int(tipo)<num:    #sugiriendo otra entrada en caso de ser necesario
            out=int(tipo)
            return out
        else:
            print("No tiene es opcion, escoja alguna disponible")
            out=val_num(input(":"),num)
            return out
    else:
        print("No es aceptable. Ingrese de nuevo el numero")
        out=val_num(input(":"),num)
        return out

def fecha():
    print("Ingrese fecha")
    año=val_num(input("Año:"),safer)
    mes=val_num(input("Mes:"),13)
    dia=val_num(input("Dia:"),32 if mes in [1,3,5,7,8,10,12] else 31)
    fecha=dt.date(año,mes,dia)
    return fecha
        

def menu():        #imprime menú
    menu1=" \n ¿Que desea hacer? \n Crear[0] \n Editar Proyecto[1] \n Visualizar[2] \n Eliminar[3]\n Buscar[4]\n" 
    menu1+="Filtros[5]\n Estrellas[6]\n Logs[7]\n Salir[9]"
    menu1d={0:"CREAR",1:"EDITAR",2:"VISUALIZAR",3:"ELIMINAR",4:"BUSCAR",5:"FILTRAR",6:"ESTRELLAS",9:"Salir"}
    print(menu1)
    ent0=val_num(input(":"),10)
    if ent0<5 and ent0!=1:
        menu2="Desea "+menu1d[ent0]+" un:\n Jefe[0] \n Analista[1] \n Obrero[2] \n Institucion[3] \n Proyecto[4] \n"
        print(menu2)
    return ent0

def cargar(lista,funcionario):   #Es para la misión 14 donde nos piden la creación de personas y proyectos. Estos son 
    i=0                         # Como fueron solicitados, sin embargo su composision es absolutamente random y por
    salida=funcionario           # se usa la libreria random
    for f in lista:
        p=0
        q=0
        s=0
        if i==18:
            c=Ejecucion(f[0].upper(),f[1],dt.date(f[2],f[3],f[4]),f[5],f[6],f[7])
            chief=salida[0][rd.randint(0,2)]
            c.incluir_jefe(chief)
            chief.incluir_proyecto(c)
            while p<rd.randint(1,4):
                t=salida[1][rd.randint(0,4)]
                if not t in c.analista:
                    c.analista.append(t)
                    t.incluir_jefe(chief)
                    t.incluir_proyecto(c)
                p+=1
            while q<rd.randint(1,4):
                t=salida[2][rd.randint(0,4)]
                if not t in c.obrero:
                    c.obrero.append(t)
                    t.incluir_jefe(chief)
                    t.incluir_proyecto(c)
                q+=1
            while s<2:
                t=salida[3][rd.randint(0,2)]
                if not t in c.instituciones:
                    c.instituciones.append(t)
                s+=1
            salida[4].append(c)
        elif i>=16:  
            c=Concientizacion(f[0].upper(),f[1],dt.date(f[2],f[3],f[4]),f[5],f[6],f[7])
            chief=salida[0][rd.randint(0,2)]
            c.incluir_jefe(chief)
            chief.incluir_proyecto(c)
            while p<rd.randint(1,4):
                t=salida[1][rd.randint(0,4)]
                if not t in c.analista:
                    c.analista.append(t)
                    t.incluir_jefe(chief)
                    t.incluir_proyecto(c)
                p+=1
            while q<rd.randint(1,4):
                t=salida[2][rd.randint(0,4)]
                if not t in c.obrero:
                    c.obrero.append(t)
                    t.incluir_jefe(chief)
                    t.incluir_proyecto(c)
                q+=1
            while s<2:
                t=salida[3][rd.randint(0,2)]
                if not t in c.instituciones:
                    c.instituciones.append(t)
                s+=1
            salida[4].append(c)
        elif i>=13:
            c=Instituciones(f[0].upper(),f[1],f[2])
            salida[3].append(c)
        elif i>=8:
            c=Obrero(f[0].upper(),f[1],dt.date(f[2],f[3],f[4]))
            salida[2].append(c)
        elif i>=3:
            c=Analista(f[0].upper(),f[1],dt.date(f[3],f[4],f[5]),f[2])
            salida[1].append(c)
        elif i<=2:
            c=Jefe(f[0].upper(),f[1],dt.date(f[2],f[3],f[4]))
            salida[0].append(c)
        i+=1
    return salida


# In[6]:


#Funciones de Creación
def impresion_lista(lista):        #Permite la impresion de la lista que permite seleccionar a todas las personas de 
    if len(lista)>0:               #interes y cuando se desea incorporar a los agentes a los proyectos
        for i in range(len(lista)):
            if lista[i].cargo=="jefe" or lista[i].cargo=="obrero": 
                print(lista[i].name+" ["+str(i)+"]")
            else:
                print(lista[i].name+" Especialidad:"+lista[i].especialidad+" ["+str(i)+"]")
    else:
        print("No hay nombres disponibles, debe crear al menos un individuo")

def crear_jefe(lista):                                   #Las primeras cuatro funcines permite la creacion de las personas
    nombre=input("Nombre:").upper()                      #y las instituciones involucradas. Permite la solicitud de todos
    edad=val_num(input("Edad:"),safer)                   #los campos necesarios para la creacion de obreros, analistas
    date=fecha()                                         #jefes o instituciones. Los proyectos se explican mas adelante
    jefe=Jefe(nombre,edad,date)
    lista.append(jefe)

def crear_analista(lista):
    nombre=input("Nombre:").upper()
    edad=val_num(input("Edad:"),safer)
    date=fecha()
    especialidad=input("Especialidad:").upper()
    analista=Analista(nombre,edad,date,especialidad)
    lista.append(analista)
    
def crear_obrero(lista):
    nombre=input("Nombre:").upper()
    edad=val_num(input("Edad:"),safer)
    date=fecha()
    obrero=Obrero(nombre,edad,date)
    lista.append(obrero)

def crear_institucion(lista):
    nombre=input("Nombre:").upper()
    print(menuIt)
    ent0=val_num(input(":"),3)
    tipo=menuItd[ent0]
    if tipo=="Economico":
        print(menuIe)
    else:
        print(menuIa)
    ent1=val_num(input(":"),3)
    estado=menuIad[ent1]
    institucion=Instituciones(nombre,tipo,estado)
    lista.append(institucion)

def crear_proyecto(lista,funcionarios,ent,name):            #esta funcion permite la crecion de los proyectos. 
    if ent==0: nombre=input("Nombre:").upper()
    else: nombre=name                                        #dependiendo del estado que esten da los campos necesarios
    print(menuPest)                                          #en caso de estar en planificacion se guarda como un proyecto 
    estado=val_num(input("Estado:"),3)                       #en carpet para su posterior edicion
    if estado!=0:
        descripcion=input("Descripcion:")
        date=fecha()
        print(menuPt)
        ent0=val_num(input(":"),2)
        print("El proyecto es de "+menuPtd[ent0])
        if ent0==0:
            tema=input("Tema:")
            print(menuPCi)
            ent1=val_num(input(":"),4)
            impacto=menuPCid[ent1]
            proy=Concientizacion(nombre,descripcion,date,tema,impacto,menuPestd[estado])
        elif ent0==1:
            ciudad=input("Ciudad: ")
            costo=val_num(input(":$"),safer)
            proy=Ejecucion(nombre,descripcion,date,ciudad,costo,menuPestd[estado])
            print("Seleccionar Jefe:")
        impresion_lista(funcionarios[0])
        ent2=val_num(input(":"),len(funcionarios[0]))
        chief=funcionarios[0][ent2]
        proy.incluir_jefe(chief)
        chief.incluir_proyecto(proy)
        print("Seleccionar Analistas")
        impresion_lista(funcionarios[1])
        cont=0
        lt1=[]
        while cont!=1:
            ent3=val_num(input("Agregar a:"),len(funcionarios[1]))
            indv=funcionarios[1][ent3]
            if not indv in lt1:
                lt1.append(indv)
                indv.incluir_jefe(chief)
                indv.incluir_proyecto(proy)
            print("Agregar mas [0] Continuar[1]")
            cont=val_num(input(":"),2)
        proy.incluir_analistas(lt1)
        print("Seleccionar Obreros")
        impresion_lista(funcionarios[2])
        cont=0
        lt2=[]
        while cont!=1:
            ent4=val_num(input("Agregar a:"),len(funcionarios[2]))
            indv=funcionarios[2][ent4]
            if not indv in lt2:
                lt2.append(indv)
                indv.incluir_jefe(chief)
                indv.incluir_proyecto(proy)
            print("Agregar mas [0] Continuar[1]")
            cont=val_num(input(":"),2)
        proy.incluir_obrero(lt2)
        print(proy)
        lista.append(proy)
    else:
        c=Proyecto(nombre,"","",menuPestd[estado])    
        lista.append(c)


# In[7]:


#Funciones de Visualización
#Imprime la lista que sea solicitada
def imprimir(lista):
    for e in lista:
        print (e)
        


# In[8]:


#Funciones de Filtrado
def ordDate(e):  #Permite el ordenamiento por fecha de inscripción
    return e.date

def buscador(nombre,listas,caso): #Permite buscar un individuo o persona para saber sus proyectos
    lt=[]   
    for e in listas:
        p=e.name
        if nombre in p  :
            lt.append(e)
    if len(lt)>0 and caso==0:
        for e in lt:
            print(e)
    elif len(lt)>0 and caso==1:   #Retorna el individuo buscado en caso de ser necesario
        for i in range(len(lt)):
            print(lt[i].name,"["+str(i)+"]")
            ent1=val_num(input(":"),len(lt))
            out=lt[ent1]
            return out
    else:
        print("No se encontro resultado alguno")
        return 0
def filtrador(tipos,listas):  #Permite la filtracion requerida en el enunciado si es por categoria o fecha
    if tipos=="Categoria":
        lt=[]
        print("Concientizacion[0] o Ejecucion[1]")
        ent2=val_num(input(":"),2)
        if ent2==0:
            for e in listas:
                if e.tipo=="Concientizacion":
                    lt.append(e)           
        else:
            for e in listas:
                if e.tipo=="Ejecucion":
                    lt.append(e)
        return lt
        
    else:
        f=sorted(listas, key=ordDate)
        return f


# In[9]:


#Voluntario estrella
def numOrd(lista):                                              #Para poder ordenar la cantidad de proyectos
    return lista[1]                                             #Toma todos los individuos y los ordena de mas a menos.
def estrella(lista):                                            #Luego entrega los tres primeros
    estrella=[] 
    i=0
    q=0
    while i<3:
        for e in lista[i]:
            cant=len(e.proyectos)
            estrella.append([e.name,cant])
        i+=1
    estrella.sort(key=numOrd,reverse=True) 
    print(estrella[:3])


# In[10]:


#Eliminar
    
def eliminar(objeto,lista,ent):              #Eliminar al individuo buscado o bien al proyecto. Elimina en todas las partes
    identificacion=id(objeto) 
    cont1=True                              #donde se encuentra el proyecto o los individuos, es decir listas ajenas y 
    if objeto.cargo=="proyecto":            #generales
        i=0
        while i<3:
            for e in lista[i]:
                if e.cargo=="obrero" or e.cargo=="analista":
                    lista3=e.jefes
                lista2=e.proyectos
                j=0
                cont=True
                while cont and j<len(lista2):
                    if id(lista2[j])==identificacion:
                        if e.cargo=="obrero"or e.cargo=="analista":
                            lista3.pop(j)
                        lista2.pop(j)
                        cont=False
                        print("Eliminado de su(s) "+cargos[i])
                    else:
                        j+=1
            i+=1
        cont=True
        i=0
        while cont and i<len(lista[4]):
            if id(lista[4][i])==identificacion:
                lista[4].pop(i)
                print("Eliminado como proyecto")
                cont=False
            i+=1
        if cont:
            print("No se elimino ningun proyecto")
        
    elif objeto.cargo=="analista" or objeto.cargo=="obrero":
        cont1=True
        for e in lista[4]:
            cont=True
            if objeto.cargo=="analista":
                    lista2=e.analista
                    ent3=1
            else:
                lista2=e.obrero 
                ent3=2
            p=0
            while p<len(lista2):
                if id(lista2[p])==identificacion:
                    lista2.pop(p)
                    cont=False
                    cont1=False
                    p=0
                    print("Eliminado de su proyecto \n Eliminado de su jefe")
                p+=1
        p=0
        while  p<len(lista[ent3]):
            if id(lista[ent3][p])==identificacion:
                lista[ent3].pop(p)
                print("Eliminado como" +cargos[ent3])
            p+=1
        if cont:
            print("No se elimino ningun individuo")

                    
    if cont1:
           print("No fue eliminado de nada")      


# In[11]:


#Logs
def logs(listas):                                      #Permite la asignacion de acciones por parte de un jefe de proyecto
    ent1=input("Nombre proyecto:").upper()             #a un analista o obrero determinado. De la misma forma permite la
    proyecto=buscador(ent1,listas[4],1)                # visualización de los logs de un proyecto
    if proyecto!=0:
        print("Orden[0] Vizualizar[1]")
        ent2=val_num(input(":"),2)
        if ent2==0:
            orden=input("Orden:")
            ent2=val_num(input("Ejecuta Analista[1] u Obrero[2]:"),3)
            if ent2==1:
                lt=proyecto.analista
            else:
                lt=proyecto.obrero
            print("Seleccionar")
            impresion_lista(lt)
            ent3=val_num(input(":"),len(lt))
            indv=lt[ent3].accionar(orden)
            jefe=proyecto.jefe.accionar(orden)
            proyecto.incluir_logs(orden)
        else:
            t=""
            for e in proyecto.logs:
                t+=e+" "
            print(t)


# In[12]:


#Funciones de edicion

def edit_proyecto(listas):                                   #Permite la edicion de los campos mas importantes de un
    print("Editar proyectos")                                #Proyecto
    ent1=input("Nombre proyecto:").upper()
    proy=buscador(ent1,listas[4],1)
    play=True
    while play and proy!=0:
        print(menuEp)
        ent1=val_num(input(":"),5)
        if ent1==0:
            print(proy.name+"\n Mantener[0] Cambiar[1]")
            if val_num(input(":"),2)==1: proy.name=input("Nuevo nombre:").upper()
        elif ent1==1:
            print(proy.desc+"\n Mantener[0] Cambiar[1]")
            if val_num(input(":"),2)==1: proy.desc=input("Nuevo nombre:")
        elif ent1==2:
            print(proy.date+"\n Mantener[0] Cambiar[1]")
            if val_num(input(":"),2)==1: proy.date=fecha()
        elif ent1==3:
            print(proy.est+"\n Mantener[0] Cambiar[1]")
            if val_num(input(":"),2)==1: 
                print(menuPest)
                proy.est=menuPestd[val_num(input(":"),3)]
        elif ent1==4:
            print(proy.jefe.name+"\n Mantener[0] Cambiar[1]")
            if val_num(input(":"),2)==1:
                impresion_lista(listas[0])
                proy.jefe=funcionario[0][val_num(input(":"))]
        if proy.tipo=="Concientizacion":
                print(menuEpC)
                ent2=val_num(input(":"),3)
                if ent2!=3:
                    if ent2==0:
                        print(proy.tema+"\n Mantener[0] Cambiar[1]")
                        if val_num(input(":"),2)==1: proy.tema=input("Nuevo nombre:").upper()
                    elif ent2==1:
                        print(proy.impacto+"\n Mantener[0] Cambiar[1]")
                        if val_num(input(":"),2)==1:
                            print(MenuPCi)
                            proy.impacto= menuPCid[val_num(input(":"),4)]
        elif proy.tipo=="Ejecucion":
            print(menuEpE)
            ent2=val_num(input(":"),3)
            if ent2!=3:
                if ent2==0:
                    print(proy.city+"\n Mantener[0] Cambiar[1]")
                    if val_num(input(":"),2)==1: proy.city=input("Nuevo nombre:").upper()
                elif ent2==1:
                    print(str(proy.cost)+"\n Mantener[0] Cambiar[1]")
                    if val_num(input(":"),2)==1: proy.cost=val_num(input("Nuevo costo:"),safer)
        elif proy.tipo=="Planificacion":
            name=proy.name
            crear_proyecto(listas[4],listas,1,name)
            play=False
                            
        print("Salir?[0] Continuar [1]")
        if val_num(input(":"),2)==0: play=False
                
        


# In[13]:


datos=[["Frank Lopulus",21,2016,10,31], ["Mouses Laplace",21,2015,7,30], ["Funes Marquez",52,2015,12,4],
["Laury Collins",30,"Electrico",2014,5,4],
["Mike Yeomans",65,"Geografo",2013,4,30],["Bernnie Von Guido",47,"Diseno",2011,2,5],
["George Sanders",42,"Matematico",2018,9,14], 
["Marie Platini",35,"Ambientalista",2016,8,24],  ["Jean-Luc Picard",63,2017,5,23], ["James Kirk",50,2017,3,31],
["Damien Higgins",26,2019,4,5], ["Lucy Hamas",24,2014,5,9], ["Guadalupe Ramos",35,2013,8,17],
["Water ONG","Tecnico","Publica"], ["Amazonas","Gestion","Social"], ["Mountain Fund","Economico","Privada"], 
 ["Save the Water Org","Manejo de recursos hidricos",1990,11,12,"Agua","Nacional","Finalizado"], 
 ["Mineria conciente","Ayuda sobre explotacion minera sustentable",1997,2,24,"Mineria","Local","Finalizado"], 
 ["Araucaria","Conservacion de parques nacionales",1993,6,5,"Aysen",1574840000,"Finalizado"]]


# CODIGO PRINCIPAL

# In[ ]:


#Listas
jefes=[]
analistas=[]
obreros=[]
instituciones=[]
proyectos=[]
carpeta=[]
listas=[jefes,analistas,obreros,instituciones,proyectos,carpeta]

print("Bienvenido SILVANUS, la plataforma de proyectos por el medio ambiente")
funcionario=cargar(datos,listas)
play=True
while play:
    ent0=menu()
    if ent0==0:
        ent1=val_num(input(":"),5)
        if ent1==0:
            crd=crear_jefe(jefes)
        elif ent1==1:
            crd=crear_analista(analistas)
        elif ent1==2:
            crd=crear_obrero(obreros)
        elif ent1==3:
            crd=crear_institucion(instituciones)
        elif ent1==4:
            crd=crear_proyecto(proyectos,funcionario,0,"")
    elif ent0==1:
        edit_proyecto(funcionario)
    elif ent0==2:
        ent1=val_num(input(":"),5)
        if ent1==0:
            crd=imprimir(funcionario[0])
        elif ent1==1:
            crd=imprimir(funcionario[1])
        elif ent1==2:
            crd=imprimir(funcionario[2])
        elif ent1==3:
            crd=imprimir(funcionario[3])
        elif ent1==4:
            crd=imprimir(funcionario[4])   
    elif ent0==3:
        ent1=val_num(input(":"),5)
        nombre=input("Nombre:").upper()
        ent2=buscador(nombre,funcionario[ent1],1)
        if ent2!=0:
            eliminar(ent2,funcionario,ent1)
    elif ent0==4:
        ent1=val_num(input(":"),5)
        nombre=input("Nombre:").upper()
        buscador(nombre,funcionario[ent1],0)
    elif ent0==5:
        print("Categoria[0]-Fecha[1]")
        ent1=val_num(input(":"),2)
        sald=filtrador(menuFd[ent1],funcionario[4])
        for e in sald:
            print(e.name)
    elif ent0==6:
        print(estrella(funcionario))
    elif ent0==7:
        logs(funcionario)
    elif ent0==9:
        play=False
        print("Gracias por ocupar SILVANUS")


# In[ ]:




