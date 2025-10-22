"""
Queue (Cola) implementada con lista doblemente enlazada.

TODO:
- Implementa DoubleNode (value, prev, next)
- Implementa Queue con operaciones: enqueue, dequeue, peek, is_empty, size
- Enqueue al final (tail) y dequeue al inicio (head) para O(1)

Sugerencia:
- Mantén punteros a head y tail, más un contador.
"""

class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def enqueue(self, value):
        """Inserta al final. O(1)"""
        new_node = DoubleNode(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.count += 1

    def dequeue(self):
        """Extrae el primero. O(1). Debe lanzar IndexError si está vacía."""
        if not self.head:
            raise IndexError("La cola no contiene elementos")
        value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.count -= 1
        return value

    def peek(self):
        """Retorna el primero sin extraer. O(1). IndexError si vacía."""
        if not self.head:
            raise IndexError("La cola no contiene elementos")
        return self.head.value

    def is_empty(self):
        """True si la cola está vacía. O(1)"""
        return self.count == 0

    def size(self):
        """Cantidad de elementos. O(1)"""
        return self.count
