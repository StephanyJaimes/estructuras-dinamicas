# Retos

## Reto 1 — Validador de expresión (Stack)
Implementa `validar_expresion(expresion: str) -> bool` usando `Stack` (estructuras/stack.py) para validar (), {}, [] balanceados.

## Reto 2 — Simulador de Cola (Queue)
Implementa `GestorCola` usando `Queue` (estructuras/queue.py) con:
- `agregar_persona(nombre: str, tiempo: int) -> None`
- `atender_persona() -> tuple[str,int]` (retorna (nombre, tiempo))
- `estado() -> list[str]` (nombres en orden)

## Reto 3 — Gestor de Tareas (LinkedList)
Implementa funciones sobre `DoublyLinkedList`:
- `agregar_tarea(id:int, descripcion:str, prioridad:int) -> None`
- `buscar_por_id(id:int) -> dict|None`
- `buscar_por_prioridad(prioridad:int) -> list[dict]`
