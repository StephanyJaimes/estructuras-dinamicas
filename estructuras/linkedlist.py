"""
Lista doblemente enlazada (DLL) para gestionar tareas.

TODO:
- Implementa DoubleNode (id, descripcion, prioridad, prev, next)
- Implementa DoublyLinkedList con: append, prepend, remove_by_id, find_by_id, find_by_prioridad, iter_forward, iter_backward, size
- Mantén head, tail y contador para O(1) en inserciones a extremos.

Nota:
- 'find' será O(n) lineal.
"""

class DoubleNode:
    def __init__(self, id, descripcion, prioridad):
        self.id = id
        self.descripcion = descripcion
        self.prioridad = prioridad
        self.prev = None
        self.next = None

class DoublyLinkedList:
    # TODO: implementar DLL
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, task):
        """Inserta al final. O(1)"""
        new_node = DoubleNode(task["id"], task["descripcion"], task["prioridad"])
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.count += 1

    def prepend(self, task):
        """Inserta al inicio. O(1)"""
        new_node = DoubleNode(task["id"], task["descripcion"], task["prioridad"])
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count += 1

    def remove_by_id(self, task_id):
        """Elimina por id. O(n). Retorna True si elimina, False si no."""
        current = self.head
        while current:
            if current.id == task_id:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                self.count -= 1
                return True
            current = current.next
        return False

    def find_by_id(self, task_id):
        """Retorna la tarea o None. O(n)"""
        current = self.head
        while current:
            if current.id == task_id:
                return {
                    "id": current.id,
                    "descripcion": current.descripcion,
                    "prioridad": current.prioridad,
                }
            current = current.next
        return None

    def find_by_prioridad(self, prioridad):
        """Retorna lista de tareas con esa prioridad. O(n)"""
        results = []
        current = self.head
        while current:
            if current.prioridad == prioridad:
                results.append({
                    "id": current.id,
                    "descripcion": current.descripcion,
                    "prioridad": current.prioridad,
                })
            current = current.next
        return results

    def iter_forward(self):
        """Generador hacia adelante."""
        current = self.head
        while current:
            yield current
            current = current.next

    def iter_backward(self):
        """Generador hacia atrás."""
        current = self.tail
        while current:
            yield current
            current = current.prev

    def size(self):
        """Cantidad de nodos. O(1)"""
        return self.count
