"""
Reto 1: Validador de expresión usando Stack.
Paréntesis válidos: (), {}, []

Función a implementar:
    validate_expression(expression: str) -> bool

Reglas:
- Recorre la cadena; apila aperturas; ante un cierre, desapila y compara.
- Si al final la pila queda vacía y nunca hubo desajuste -> True.

Tips:
- Usa Stack de estructuras/stack.py
"""

from estructuras.stack import Stack

PARES = {')': '(', '}': '{', ']': '['}

def validate_expression(expression: str) -> bool:
    # TODO: Implementar con Stack siguiendo las reglas de arriba.
    # Debe ser O(n) en tiempo; O(n) espacio peor caso.

    stack = Stack() # Crear una pila vacía
    for char in expression:
        # Si es un signo de apertura ({[, apilar
        if char in PARES.values():
            stack.push(char)
        # Si es un signo de cierre ]}) desapilar y comparar
        elif char in PARES:
            if stack.is_empty(): # Si la pila está vacía da error
                return False
            top = stack.pop()
            if top != PARES[char]:
                return False
        # Si no es paréntesis, se ignora
        else:
            continue  
        # Si al final la pila queda vacía, está balanceado
    return stack.is_empty()
