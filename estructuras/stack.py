"""
Stack (Pila) implementado con lista enlazada simple.

TODO:
- Implementa Node (valor, next)
- Implementa Stack con operaciones: push, pop, peek, is_empty, size
- Garantiza que push y pop sean O(1)

Sugerencia:
- Mantén referencia a la "cabeza" (top) y un contador de tamaño.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, value):
        """Inserta en el tope. O(1)"""
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        """Extrae y retorna el tope. O(1). Debe lanzar IndexError si está vacía."""
        if not self.top:
            raise IndexError("La pila no contiene elementos")
        value = self.top.value
        self.top = self.top.next
        self.count -= 1
        return value

    def peek(self):
        """Retorna el tope sin extraer. O(1). IndexError si vacía."""
        if not self.top:
            raise IndexError("La pila no contiene elementos")
        return self.top.value

    def is_empty(self):
        """True si no hay elementos. O(1)"""
        return self.count == 0

    def size(self):
        """Cantidad de elementos. O(1)"""
        return self.count
