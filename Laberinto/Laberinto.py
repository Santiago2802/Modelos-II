class nodos():
    def __init__(self,valor,pos,hijos=[]):
        self.valor=valor
        self.pos = pos
        self.hijos=hijos

    def agregarHijo(self,hijo):
        self.hijos.append(hijo)
        
    def setpos(self,pos):
        self.pos=pos

    def setHijos(self,hijos):
        self.hijos=hijos
        
raiz=nodos(0,0,[])

def buscar(arbol,pos):
    if arbol==None:
        return False
    if arbol.pos==pos:
        return True
    return buscarhijos(arbol.hijos,pos) 

def buscarhijos(hijos,pos):
    if hijos==[]:
        return False
    return buscar(hijos[0],pos) or buscarhijos(hijos[1:],pos)

def findX(Lab):
   for x in Lab:
       for y in range(len(x)):
           if x[y] == "x":
               PutTree(Lab.index(x),y,Lab, nodos(0,0,[])) 
                
def PutTree(x,y,Lab, arbol):
        raiz.setpos((x,y))
        arbol.setpos((x,y))
        raiz.setHijos([Left(x,y,arbol,Lab),Down(x,y,arbol,Lab),Up(x,y,arbol,Lab),Right(x,y,arbol,Lab)])

def Up(x,y,nodo,Lab):
    print((x,y),"Dirigirse hacia arriba")
    if(x-1>=0 and Lab[x-1][y]!="1"):
        if(buscar(nodo,(x-1,y))!=True):
            nodo.agregarHijo(nodos(Lab[x-1][y],(x-1,y),[]))
            return nodos(Lab[x-1][y],(x-1,y),[Down(x-1,y,nodo,Lab),Up(x-1,y,nodo,Lab),Down(x-1,y,nodo,Lab),Right(x-1,y,nodo,Lab)])
        else:
            return None
    else:
        return None

def Down(x,y,nodo,Lab):
    print((x,y),"Dirigirse hacia abajo")
    if(x+1<=len(Lab)-1 and Lab[x+1][y]!="1"):
        if(buscar(nodo,(x+1,y))!=True):
            nodo.agregarHijo(nodos(Lab[x+1][y],(x+1,y),[]))
            return nodos(Lab[x+1][y],(x+1,y),[Down(x+1,y,nodo,Lab),Up(x+1,y,nodo,Lab),Left(x+1,y,nodo,Lab),Right(x+1,y,nodo,Lab)])
        else:
            return None
    else:
        return None

def Left(x,y,nodo,Lab):
    print((x,y),"Dirigirse a la izquierda")
    if(y-1>=0 and Lab[x][y-1]!="1"):
        if(buscar(nodo,(x,y-1))!=True):
            nodo.agregarHijo(nodos(Lab[x][y-1],(x,y-1),[]))
            return nodos(Lab[x][y-1],(x,y-1),[Down(x,y-1,nodo,Lab),Up(x,y-1,nodo,Lab),Left(x,y-1,nodo,Lab),Right(x,y-1,nodo,Lab)])
        else:
            return None
    else:
        return None

def Right(x,y,nodo,Lab):
    print((x,y),"Dirigirse a la derecha")
    if(y+1<=len(Lab[x])-1 and Lab[x][y+1]!="1"):
        if(buscar(nodo,(x,y+1))!=True):
            nodo.agregarHijo(nodos(Lab[x][y+1],(x,y+1),[]))
            return nodos(Lab[x][y+1],(x,y+1),[Down(x,y+1,nodo,Lab),Up(x,y+1,nodo,Lab),Left(x,y+1,nodo,Lab),Right(x,y+1,nodo,Lab)])
        else:
            return None
    else:
        return None

def buscarValor(arbol,valor):
    if arbol==None:
        return False
    if arbol.valor==valor:
        return True
    return buscarhijosValor(arbol.hijos,valor)

def buscarhijosValor(hijos,valor):
    if hijos==[]:
        return False
    return buscarValor(hijos[0],valor) or buscarhijosValor(hijos[1:],valor)

def LeerLaberinto():
    return[list(linea)[:-1] for linea in open ("Laberinto.txt").readlines()]


def main():
    
    findX(LeerLaberinto())
    if(buscarValor(raiz,"y")==True):
         print("El laberinto si tiene solución")
    else:  print("El laberinto no tiene solución")

    
main()


