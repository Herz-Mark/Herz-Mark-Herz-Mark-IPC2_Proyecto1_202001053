from tkinter.constants import NO
from Nodo import Node

#inicializa la lista enlazada (Constructor)
class LinkedList:
    def __init__(self):
        self.First = None
        self.Size = 0

#Inserta valores a los nodos
    def Insert(self, Value):
        MiNodo = Node(Value) 
        if  self.Size == 0:
            self.First = MiNodo
        else:
            Current = self.First
            while Current.Next != None:
                Current = Current.Next 
            Current.Next = MiNodo
        self.Size += 1
        return MiNodo
    
    def clear(self):
        self.First = None
        self.Size = 0
    
    def get_last(self):
        if self.First == None:
            return None
        nod = self.First
        while nod.Next != None:
            nod = nod.Next
        return nod.Value


    def _len_(self):
        return self.Size

    def __str__(self):
        String = "{"
        Current = self.First
        while Current != None:
            String += str(Current)
            String += str(",")
            Current = Current.Next
        String += "}"
    
        return String

    
    