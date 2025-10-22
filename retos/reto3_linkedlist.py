"""
Reto 3: Gestor de tareas con DoublyLinkedList.

Funciones a implementar (usa DoublyLinkedList de estructuras/linkedlist.py):
    - add_task(id:int, descripcion:str, prioridad:int) -> None
    - find_by_id(id:int) -> dict|None
    - find_by_priority(prioridad:int) -> list[dict]

Nota:
- La lista interna debe almacenar dicts con llaves: id, descripcion, prioridad.
"""

from estructuras.linkedlist import DoublyLinkedList

_lista_tareas = DoublyLinkedList()

def add_task(task_id: int, descripcion: str, prioridad: int) -> None:
    # TODO: crear dict y agregar al final (append) en O(1)
    tarea = {
        "id": task_id,
        "descripcion": descripcion,
        "prioridad": prioridad
    }
    _lista_tareas.append(tarea)

def find_by_id(task_id: int):
    # TODO: delegar en DLL.find_by_id (O(n))
    return _lista_tareas.find_by_id(task_id)

def find_by_prioridad(prioridad: int):
    # TODO: delegar en DLL.find_by_prioridad (O(n))
    return _lista_tareas.find_by_prioridad(prioridad)