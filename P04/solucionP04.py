#!/usr/bin/env python
# coding: utf-8

# In[14]:


import sqlite3

connection=sqlite3.connect('p04.db')
cursor=connection.cursor()


cursor.execute('CREATE TABLE Marcas (id_marcas INTEGER,nombre TEXT,PRIMARY KEY (id_marcas))')
cursor.execute('CREATE TABLE Colores (id_colores INTEGER,nombre TEXT ,PRIMARY KEY (id_colores))')
cursor.execute('CREATE TABLE Autos (patente TEXT,id_marcas,id_colores,velocidad INTEGER,capacidad INTEGER,PRIMARY KEY (patente),FOREIGN KEY (id_marcas) REFERENCES Marcas, FOREIGN KEY (id_colores) REFERENCES Colores)')

cursor.execute('INSERT INTO Colores  VALUES (001,"Amarillo")')
cursor.execute('INSERT INTO Colores  VALUES (002,"Verde")')
cursor.execute('INSERT INTO Colores  VALUES (003,"Rojo")')

cursor.execute('INSERT INTO Marcas  VALUES (001,"Toyota")')
cursor.execute('INSERT INTO Marcas  VALUES (002,"Honda")')
cursor.execute('INSERT INTO Marcas  VALUES (003,"Pegueot")')

cursor.execute('INSERT INTO Autos  VALUES ("ABC123",001,001,100,5)')
cursor.execute('INSERT INTO Autos  VALUES ("DEF123",002,001,120,6)')
cursor.execute('INSERT INTO Autos  VALUES ("HIJ123",003,002,150,4)')
cursor.execute('INSERT INTO Autos  VALUES ("ABC321",001,002,130,5)')
cursor.execute('INSERT INTO Autos  VALUES ("DEF321",002,003,125,6)')
cursor.execute('INSERT INTO Autos  VALUES ("HIJ321",003,003,140,4)')
 
cursor.execute('SELECT DISTINCT A.patente FROM Autos A WHERE A.id_colores=001')
consulta1=cursor.fetchall()
cursor.execute('SELECT DISTINCT A.patente FROM Autos A WHERE A.velocidad%2=0')
consulta2=cursor.fetchall()
cursor.execute('SELECT DISTINCT A.patente FROM Autos A WHERE A.capacidad>A.velocidad/10')
consulta3=cursor.fetchall()
#connection.execute('SELECT DISTINCT A.patente FROM Autos A WHERE A.velocidad%2=0')

print(consulta1)
print(consulta2)
print(consulta3)

connection.commit()
cursor.close()


# In[ ]:




