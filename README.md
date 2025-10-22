# Estructuras Dinámicas — Mini Biblioteca + Retos

Este repo contiene una **mini-biblioteca de estructuras** (Stack, Queue, LinkedList) y **3 retos** aplicados. La intención es practicar TDD: primero verás **pruebas unitarias iniciales** que fallan (fase *Red*), luego implementarás el mínimo código para hacerlas pasar (*Green*), y finalmente mejorarás (*Refactor*).

## Estructuras
- `Stack` sobre lista enlazada simple.
- `Queue` sobre lista doblemente enlazada.
- `LinkedList` (doblemente enlazada) con operaciones básicas.

## Retos
- **Reto 1 (Stack):** Validador de paréntesis/llaves/corchetes.
- **Reto 2 (Queue):** Simulador de cola de atención (FIFO).
- **Reto 3 (LinkedList):** Gestor de tareas (insertar, eliminar, buscar, recorrer).

## Cómo ejecutar pruebas
```bash
python -m unittest -v
```

## Sugerencias

* Sigue el patrón AAA (Arrange, Act, Assert) en las pruebas.
* Agrega más casos (bordes, errores esperados).
* Documenta complejidades Big-O en los READMEs de cada carpeta.

