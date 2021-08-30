from tkinter import Tk
from tkinter.filedialog import askopenfilename
from xml.etree import ElementTree as ET 
from LinkedList import LinkedList
import graphviz
Lista = LinkedList()
Lista_new = LinkedList()
ListaX = LinkedList()
ListaY = LinkedList()
X_new = LinkedList()
Y_new = LinkedList()
d = graphviz.Digraph(filename='matriz')
counter_mx = 0

def Menu():
    op = 0
    while op!=6:
        print("")
        print("================MENÚ================")
        print("||       1. Cargar Archivo        ||")
        print("||      2. Procesa Archivo        ||")
        print("|| 3. Escribir Archivo de Salida  ||")
        print("||    4. Datos del Estudiante     ||")
        print("||      5. Generar Gráfica        ||")
        print("||           6. Salida            ||")
        print("====================================")
        print("")
        print("ingrese una opcion:")
        op = int(input())

        if op==1:
            #Con este comando ejecutamos nuestro filedialog
            Tk().withdraw()
            #Obtenemos la ruta del archivo que escogimos
            filename = askopenfilename()

            #leemos nuestro archivo por medio de la ruta obtenida con el filedialog
            tree = ET.parse(filename)
            terrenos = tree.findall('terreno')

            for terreno in terrenos:
                Lista.Insert(terreno.attrib['nombre'])
                ListaX.Insert(terreno.attrib['nombre'])
                ListaY.Insert(terreno.attrib['nombre'])
                posiciones = terreno.findall("posicion")
                for posicion in posiciones:
                    Lista.Insert(int(posicion.text))
                    ListaX.Insert(posicion.attrib['x'])
                    ListaY.Insert(posicion.attrib['y'])
             
        
            def procesar_terreno(nombre):
                node = Lista.First
                PosX = ListaX.First
                PosY = ListaY.First
                Lista_new.clear()
                X_new.clear()
                Y_new.clear()
                while node != None:
                    if str(node) == nombre:
                        node = node.Next
                        PosX = PosX.Next
                        PosY = PosY.Next
                        while node != None and -1 == str(node).find("terreno"):
                            Lista_new.Insert(node)
                            X_new.Insert(PosX)
                            Y_new.Insert(PosY)
                            node = node.Next
                            PosX = PosX.Next
                            PosY = PosY.Next
                    elif node!= None:
                        node = node.Next
                        PosX = PosX.Next
                        PosY = PosY.Next

            def Size():
                PosX = X_new.First
                PosY = Y_new.First
                while PosX.Next != None:
                    PosX = PosX.Next
                    PosY = PosY.Next
                j = [int(str(PosX)), int(str(PosY))]
                return(j)
                
            def matrix():
                x = Size()[0]
                y = Size()[1]
                data = Lista_new.First
                array = [[0]*x for i in range(y)]
                    
                for n in range(x):
                    for m in range(y):
                        array[m][n] = str(data)
                        data = data.Next         
                        
                return(array)
        
            def matrix_aux():
                contador = 0
                x = Size()[0]
                y = Size()[1]
                array = [[0]*x for i in range(y)]

                for n in range(y):
                    for m in range(x):
                        array[n][m] = contador
                        contador +=1
                print(contador)
                return(array)

        elif op==2:
            print("Ingrese el nombre del terreno")
            procesar_terreno(input())
            for n in matrix():
                print(n)
        
        elif op==3:
            print("Escribir archivo de salida")

        elif op==4:
            print("Kevin Mark Hernández Chicol")
            print("202001053")
            print("Introduccion a la programación y computación 2 Seccion \"A\"")
            print("Ingeniería en Ciencias y Sistemas")
            print("4to Semestre")
        
        elif op==5:
            print("Generar Grafica")
           

#Matriz de ejemplo
            matriz = matrix()

            def declararNodos(listaFila):#Aca se definen las filas al mismo nivel
                global d    
                global counter_mx 
                with d.subgraph() as s:
                    s.attr(rank='same')        
                    for i in listaFila:
                        s.node(str(counter_mx), str(i))
                        counter_mx+=1

            def apuntarNodosHorizontales(lista):#Aca se apuntan los nodos de cada fila
                global d
                contador = 0
                for i in lista:
                    if contador <= len(lista) and contador >= 1:
                        d.edge(str(lista[contador - 1]), str(lista[contador]))
                    contador += 1    

            def apuntarNodosVerticales(matriz):#Aca se apuntan los nodos de cada columna
                contador1 = 0
                for i in matriz:
                    contador2 = 0
                    for j in i:
                        if (contador2 < len(i) and contador2 >= 1 ):
                            if(contador2 == 1) and contador1 < len(matriz) - 1:
                                d.edge(str(i[contador2-1]), str(matriz[contador1 + 1][contador2-1]))
                            if contador1 < len(matriz) - 1:
                                d.edge(str(i[contador2]), str(matriz[contador1 + 1][contador2]))
                        contador2 += 1
                    contador1 += 1

            for i in matriz:
                declararNodos(i)

            for i in matrix_aux():
                apuntarNodosHorizontales(i)

            apuntarNodosVerticales(matrix_aux())

            d.view()
            d.clear()
            
        
        elif op==6:
            print("Adios")
        
        else:
            print("Eliga una opcion correcta")


