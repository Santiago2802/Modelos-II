class Nodo:
    def __init__(self,valor,izq=None,der=None):
        self.valor=valor
        self.izq=izq
        self.der=der

def buscar (arbol,valor):
    if arbol==None:
        return False
    if arbol.valor==valor:
        return True
    if arbol.valor<valor:
        return buscar(arbol.der,valor)
    return buscar(arbol.izq,valor)

def sumar(arbol):
    if arbol==None:
        return 0
    return sumar(arbol.izq)+arbol.valor+sumar(arbol.der)

def a_lista(arbol):
    if arbol==None:
        return []
    return a_lista(arbol.izq)+[arbol.valor]+a_lista(arbol.der)


def insertar(arbol,valor):
    if arbol==None:
        return Nodo(valor)
    if arbol.valor < valor:
        return Nodo(arbol.valor,arbol.izq,insertar(arbol.der,valor))
    return Nodo(arbol.valor,insertar(arbol.izq,valor),arbol.der)

def a_arbol(arbol,lista):
    if lista == []:
        return arbol
    return a_arbol(insertar(arbol, lista[0]), lista[1:])
    

def  main():
    
    tree=Nodo(25,Nodo(10,Nodo(5),Nodo(18)),Nodo(40,None,Nodo(50)))

    print("Buscar el 10: " + str(buscar(tree,10)))
    print("Sumar el Árbol: " + str(sumar(tree)))
    print("Mi Árbol a Lista: " + str(a_lista(tree)))

   #Insertar Nodos A un Árbol
    tree=insertar(tree,15)
    tree=insertar(tree,1)
    tree=insertar(tree,120)
    
    print("Mi Árbol con Nodo 15, 1 y 120 : " + str(a_lista(tree)))

    Lista = [6,7,3,87,12,789,2,4]
    #Insertar lista a Un árbol existente
    Lista_Arbol = a_arbol(tree,Lista)

    print("Mi Lista a Árbol: " + str(a_lista(Lista_Arbol)))
main()





