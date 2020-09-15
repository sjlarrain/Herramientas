#!/usr/bin/env python
# coding: utf-8

# In[5]:


from copy import deepcopy as dp
def problemaP03(lista,buscado):
    def sumar(a,b):
        return b+a
    def restar(a,b):
        return b-a
    
    def numero(a,buscado,b=0):
        sol=0
        if sumar(a,b)==buscado:
            sol+=1
        if restar(a,b)==buscado:
            sol+=1
        solution.append(sol)
        return [sumar(a,b),restar(a,b)]

    def cont(lt,buscado,res=0):
        if len(lt)>=1:
            sol=res+numero(lt[0],buscado)
            konts=cont(lt[1:],sol[0])
            kontr=cont(lt[1:],sol[1])
    
    def solver(arbol,lista,buscado):
        ltCN=dp(arbol)
        ltCN.append(lista[0])
        ltSN=dp(arbol)
        if len(lista[1:])>0:
            cont(ltCN,buscado,lista[1:])
            cont(ltSN,buscado,lista[1:])
    
    global solution
    solution=[]
    arbol=[]
    solver(arbol,lista,buscado)
    return solution
            
            
            
            
    


# In[6]:


lista=[4, 8, -4, 1]
print(problemaP03(lista,4))


# In[ ]:




