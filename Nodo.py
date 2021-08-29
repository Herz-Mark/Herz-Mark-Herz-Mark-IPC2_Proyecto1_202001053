class Node:
    #Inicializa el nodo (Constructor)
    def __init__(self, Value):
        self.Value = Value
        self.Next = None

    def __str__(self):
        return str(self.Value)
