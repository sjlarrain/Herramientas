#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sqlite3
def total_filas(cursor, table_name):
    cursor.execute('SELECT COUNT(*) FROM {}'.format(table_name)) #Cuenta la cantidad de datos
    count = cursor.fetchall()
    return count[0][0]


def total_columnas(cursor, table_name):
    cursor.execute('PRAGMA TABLE_INFO({})'.format(table_name))#Da la cantidad de clumnas
    info = len(cursor.fetchall())#Devuelve el largo de la lista que es equivalente a la cantidad de columnas
    return info

def consultas(cursor, tabla, restriccion,elemento="*"):
    comand='SELECT{2} FROM {0} X WHERE X.{1}'.format(tabla,restriccion,elemento)#Generador de consultas
    c.execute(comand)
    x=c.fetchall()
    return x

def consulta_columna(cursor,tabla,columna,limite=""): #Generador de consultas
    comand='SELECT  X.{1} FROM {0} X {2}'.format(tabla,columna,limite)
    c.execute(comand)
    return c.fetchall()
def creador_tabla(cursor,nombre,keys,primaria=[],foraneas=[]): #Creador de tablas
    data=keys+primaria+foraneas
    datos=",".join(data)
    print(datos)
    cursor.execute('CREATE TABLE {} ({})'.format(nombre,datos))
conn=sqlite3.connect('eod.db')
c=conn.cursor()


# # MISION 1

# In[ ]:


M1=[]
c.execute("SELECT name FROM sqlite_master WHERE type='table';") #Obtiene todas las tablas de la base
names=c.fetchall() 
for e in names: #Recorre las tablas y obtiene sus filas y columnas
    filas=total_filas(c,e[0])
    columnas=total_columnas(c,e[0])
    M1.append([e[0],filas,columnas])
print(M1) #Devuelve el resultado


# # MISION 2

# In[ ]:


M2=c.execute('SELECT* FROM Hogares H WHERE H.NumPer>=3 LIMIT 10') #Obtiene los 10 primeros individuos que cumplen la
M2_r=c.fetchall()                                               #condicion impuesta
print(M2_r)


# # MISION 3

# In[ ]:


M3=[]
errables=[('DistanciaViaje','DistEuclidiana'),('DistanciaViaje','DistManhattan'),('Viajes','HoraIni'),
          ('Viajes','HoraFin'),('Viajes','HoraMedia'),('Viajes','TiempoViaje')] #Se busco opciones que podrían tener numero
                                                                                #Negativos
for e in errables:
    g=consultas(c,e[0],e[1]+'<0') #Se generaba una consulta con la condición
    if len(g)>0: #Si la respuesta era mayor a cero se le consideraba como errable
        M3.append(e)
print(M3)


# # MISION 4

# In[ ]:


columnas=dict()
for e in names:        #Obteniamos la tabla y sacabamos sus columnas
    columnas_tabla=[]
    c.execute('PRAGMA table_info([{}])'.format(e[0]))
    x=c.fetchall()
    for f in x:
        columnas_tabla.append(f[1]) 
    columnas.update({e[0]:columnas_tabla}) #Haciamos un diccionario con la informacion de cada tabla con sus colunas

for e in columnas.keys(): #Recorremos cada tabla
    cambios=[]
    for f in columnas[e]:
        x=consulta_columna(c,e,f,'LIMIT 1') #Sacamos solo el primer resultado para analizarlo
        if str(x[0][0]).isdigit(): #Si contenia digito la consideramos como elemento a cambiar
            cambios.append(f)
    col=[]
    for f in columnas[e]: #recorremos las columnas de la tabla
        if f in cambios: #Si estaba en los cambios se le aplica un cambio a INTEGER de lo contrario queda en TEXT
            elem=str(f)+r" INTEGER"
        else:
            elem=str(f)+r' TEXT' 
        col.append(elem)
    if "Personas" in columnas[e]: #Adjuntamos las primary key necesarias
        if e=="Personas":
            col.append('PRIMARY KEY (Persona)')
        else:
            col.append('FOREIGN KEY (Persona) REFERENCES Personas')
    if "Hogar" in columnas[e]:
        if e=="Hogares":
            col.append('PRIMARY KEY (Hogar)')
        else:
            col.append('FOREIGN KEY (Hogar) REFERENCES Hogares')
    if "Viaje" in columnas[e]:
        if e=="Viajes":
            col.append('PRIMARY KEY (Viaje)')
        else:
            col.append('FOREIGN KEY (Viaje) REFERENCES Viajes')
    campos=",".join(col)   #Creamos los elementos para la creacion
    campos_nt=",".join(columnas[e])
    c.execute('ALTER TABLE {} RENAME TO fake'.format(e)) #Cambiamos el nombre de la tabla
    c.execute('CREATE TABLE {} ({})'.format(e,campos)) #Creamos una nueva tabla
    c.execute('INSERT INTO {0}({1}) SELECT {1} FROM fake'.format(e,campos_nt))#Insertamos los datos de fake a la nueva tabla
    c.execute('DROP TABLE main."fake"')#elimanos fake
conn.commit()  


# # MISION 5

# In[ ]:


M5_aC='''SELECT X.Persona, X.Sexo, Y.Edad, X.LicenciaConducir 
FROM Personas X, EdadPersonas Y 
WHERE X.Sexo=1 
AND X.LicenciaConducir!=1 LIMIT 100''' #Consulta y obtenemos los 100 primeros datos para trabajar
M5_a=c.execute(M5_aC)
M5_ar=c.fetchall()
key_tablaM5_b=['Persona INTEGER', 'Sexo INTEGER', 'Edad INTEGER', 'LicenciaConducir TEXT'] #Aplicamos los contenidos a
primaryKey_tablaM5_b=['FOREIGN KEY (Persona) REFERENCES Personas']                         #para la tabla a crear
M5_tabla=creador_tabla(c,'HombresConductores',key_tablaM5_b,primaryKey_tablaM5_b) #Creamos la tabla
for e in M5_ar:
    c.execute('INSERT INTO HombresConductores VALUES({},{},{},"{}")'.format(e[0],e[1],e[2],e[3])) #Introducimos los valores
consultas(c,'HombresConductores','Edad>29 AND X.Edad<46') #Nueva consulta
M5_br=c.fetchall() #Obtenemos resultados y los retornamos con el print
print(M5_br) 
conn.commit()


# # MISION 6

# In[ ]:


class Persona:
    def __init__(self,rut,edad,sexo,comuna): #Clase persona con los datos exigidos
        self.rut=rut
        self.edad=edad
        if sexo==1:
            self.sexo="M"
        else:
            self.sexo="F"
        self.comuna=comuna
    def __str__(self):
        return ('Rut:{},Edad:{},Sexo:{},Comuna{}'.format(self.rut,self.edad,self.sexo,self.comuna))
def m6_funcion(c,distancia,modo): #Se hace la consulta que se exige
    M6_c=c.execute('''SELECT X.Persona, X.Sexo, Y.Edad, Z.Comuna 
                        FROM Viajes U,DistanciaViaje W, Personas X, EdadPersonas Y, Hogares Z 
                        WHERE W.DistEuclidiana>{} AND U.MediosUsados={} LIMIT 10'''.format(distancia,modo))
    M6_r=c.fetchall() #Obtenemos los datos
    personas=[]
    for e in M6_r: #Creamos un objeto con los datos exigidos
        people=Persona(e[0],e[1],e[2],e[3])
        personas.append(people)
    personas.append(Persona(M6_r[0],M6_r[1],M6_r[2],M6_r[3])) #Los guardamos en la lista para ser devuelto
    return personas

M6_response=m6_funcion(c,100000000,3)


# # MISION 7

# In[ ]:


class Persona:
    def __init__(self,rut,edad,sexo,comuna,convivientes,vehiculos,bicicletas):
        self.rut=rut
        self.edad=edad
        if sexo==1:
            self.sexo="M"
        else:
            self.sexo="F"
        self.comuna=comuna
        self.convivientes=convivientes
        self.bicicletas=bicicletas
        self.vehiculos=vehiculos
    def __str__(self):
        return ('Rut:{},Edad:{},Sexo:{},Comuna:{},N°Habitantes:{},N°Bicicletas{},N°Vehiculos{}'.format(self.rut,self.edad,self.sexo,self.comuna,self.convivientes,self.bicicletas,self.vehiculos))

def m7_funcion(c,sexo,edad): #Funcion con los parametros para la consulta a realizar
    if sexo=="M":
        sexo=1
    else:
        sexo=2
    c.execute('''SELECT DISTINCT X.Persona, X.Sexo, Y.Edad, Z.Comuna, V.NumPer, V.NumVeh, V.NumBicAdulto, V.NumBicNino 
                FROM Hogares V, Viajes U,DistanciaViaje W, Personas X, EdadPersonas Y, Hogares Z 
                WHERE Y.Edad={} AND X.Sexo={} LIMIT 10'''.format(edad,sexo))
    M7_r=c.fetchall()
    personas=[]
    for e in M7_r: #Recorremos y creamos la persona deseada con los componentes
        people=Persona(e[0],e[1],e[2],e[3],e[4],e[5],e[6]+e[7])
        personas.append(people)
    return personas

M7_response=m7_funcion(c,"F",30)

    


# # MISION 8

# In[ ]:


class Persona:
    def __init__(self,rut,edad,sexo,comuna,num_viajes,distancia):
        self.rut=rut
        self.edad=edad
        if sexo==1:
            self.sexo="M"
        else:
            self.sexo="F"
        self.comuna=comuna
        self.num_viajes=num_viajes
        self.distancia=distancia
    def __str__(self):
        return ('Rut:{},Edad:{},Sexo:{},Comuna{},N°Viajes:{},Distancia:{}'.format(self.rut,self.edad,self.sexo,self.comuna,self.num_viajes,self.distancia))

def M8_funcion(c,comuna):
    c.execute('''SELECT X.Persona, Y.Edad, X.Sexo, Z.Comuna, X.Viajes 
                FROM Personas X, EdadPersonas Y, Hogares Z 
                WHERE Z.Comuna="{}" LIMIT 10'''.format(comuna))
                #Obtenemos las personas que deseamos de la comuna
    M8_r1=c.fetchone()
    c.execute('''SELECT X.DistEuclidiana 
            FROM DistanciaViaje X, Viajes Y 
            WHERE Y.Persona={} LIMIT 10'''.format(M8_r1[0])) #Obtenemos la distancia de acuerdo a la respuesta de la  
    M8_r2=c.fetchall()                                      #consulta anterior
    suma_viaje=0
    for e in M8_r2: #De acuerdo a la cantidad de personas buscamos los viajes y los sumamos
        suma_viaje+=int(e[0])
    personas=[]
    personas.append(Persona(M8_r1[0],M8_r1[1],M8_r1[2],M8_r1[3],M8_r1[4],suma_viaje)) #Creamos
    
    return personas

M8_response=M8_funcion(c,"BUIN")
    


# # MISION 9

# In[ ]:


def M9_funcion(c,comuna,proposito):
    c.execute('SELECT  X.Zona FROM Hogares X WHERE X.Comuna="{}"'.format(comuna))
    zonas=c.fetchone()
    
    c.execute('''SELECT Y.Viaje, Y.HoraIni 
            FROM Hogares X, Viajes Y, Etapas Z 
            WHERE X.Zona={} AND Y.HoraIni>"6:00:00" AND Y.HoraIni<"9:00:00" AND Z.Modo={} 
            LIMIT 10'''.format(zonas[0],proposito))
    viajes=set()
    for e in c.fetchall(): #Recorremos las respuestas y agregamos los viajes por ultimo los contamos
        viajes.add(e)
    num_viajes_ida=len(viajes)
    viajes=set()
    c.execute('''SELECT Y.Viaje, Y.HoraIni 
            FROM Hogares X, Viajes Y, Etapas Z 
            WHERE X.Zona={} AND Y.HoraIni>"17:00:00" AND Y.HoraIni<"20:00:00" AND Z.Modo={} 
            LIMIT 10'''.format(zonas[0],proposito))
    for e in c.fetchall():#Exacatmente lo mismo que la ida
        viajes.add(e)
    num_viajes_vuelta=len(viajes)
    return [comuna,num_viajes_ida,num_viajes_vuelta] #Devolvemos respuesta

M9_response=M9_funcion(c,"BUIN",1)
print(M9_response)


# # MISION 10

# In[ ]:


with open("Comuna.csv",encoding="utf8") as data: #Obtenermos las comunas
    lista=[]
    for e in data.readlines()[1:]:
        x=e.strip().split(",")
        lista.append(tuple(x))
c.execute('CREATE TABLE Comunas(Codigo INTEGER,Nombre TEXT)') #Creamos tabla
for e in lista:
    c.execute('INSERT INTO Comunas(Codigo,Nombre) VALUES("{}","{}")'.format(e[0],e[1])) #Agregamos valores
conn.commit()

def M10_funcion(c):
    c.execute('''SELECT count(X.Viaje) AS contador, Y.Nombre, Z.Nombre  
    FROM Viajes X, Comunas Y,Comunas Z 
    WHERE X.ComunaOrigen!=X.ComunaDestino AND X.ComunaOrigen=Y.Codigo AND X.ComunaDestino=Z.Codigo 
    GROUP BY X.ComunaOrigen,X.ComunaDestino
    ORDER BY contador DESC
    LIMIT 10''') #Realizamos consulta pedida
    return c.fetchall()
M10_funcion(c)


# # MISION 11

# In[ ]:


def M11_funcion(c):
    c.execute('''SELECT Z.Hogar, sum(X.DistEuclidiana) AS dist 
FROM DistanciaViaje X, ViajesDifusion Y, Hogares Z, Viajes W
WHERE  Y.ModoDifusion=3 OR Y.ModoDifusion=5 OR Y.ModoDifusion=6 AND W.FactorLaboralNormal IS NOT NULL AND W.FactorLaboralEstival IS NOT NULL
GROUP BY Z.Hogar
ORDER BY  dist DESC
LIMIT 10''')
    #Buscamos los viajes de acuerdo a como fue el modo difusion. Si viajó con BIP consideramos que fue público
    #O si el viaje se tilda como público
    x=c.fetchall()
    return x
M11_funcion(c)


# In[ ]:


conn.close()


# In[ ]:




