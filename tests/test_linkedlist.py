import unittest
from retos.reto3_linkedlist import add_task, find_by_id, find_by_prioridad
from estructuras.linkedlist import DoublyLinkedList
# from retos.reto3_linkedlist import remove_by_id


class TestChallenge3LinkedList(unittest.TestCase):
    def test_add_and_find_by_id(self):
        add_task(1, "Probar DLL", 2)
        tarea = find_by_id(1)
        self.assertIsNotNone(tarea)
        self.assertEqual(tarea["id"], 1)
        self.assertEqual(tarea["descripcion"], "Probar DLL")
        self.assertEqual(tarea["prioridad"], 2)

    # - eliminar por id (cuando implementes remove)
    def test_remove_by_id(self):
        # Añade, verifica existencia, elimina y verifica que ya no existe
        from retos import reto3_linkedlist
        add_task(10, "Eliminar prueba", 3)
        self.assertIsNotNone(find_by_id(10))
        eliminado = reto3_linkedlist._lista_tareas.remove_by_id(10)
        self.assertTrue(eliminado)
        self.assertIsNone(find_by_id(10))

    # - find_by_priority devuelve múltiples tareas    
    def test_find_by_priority_multiple(self):
        add_task(1, "Tarea 1", 3)
        add_task(2, "Tarea 2", 3)
        add_task(3, "Tarea 3", 1)
        tareas = find_by_prioridad(3)
        self.assertEqual(len(tareas), 2)
        self.assertTrue(any(t["id"] == 1 for t in tareas))
        self.assertTrue(any(t["id"] == 2 for t in tareas))
    # - find_by_id inexistente -> None
    def test_find_by_id_inexistente(self):
        add_task(1, "Tarea A", 1)
        self.assertIsNone(find_by_id(99))

if __name__ == "__main__":
    unittest.main()
