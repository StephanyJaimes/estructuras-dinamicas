import unittest
from retos.reto2_queue import QueueManager

class TestChallenge2Queue(unittest.TestCase):
    def test_serve_in_fifo_order(self):
        gestor = QueueManager()
        gestor.add_person("Ana", 5)
        gestor.add_person("Luis", 3)

        nombre, tiempo = gestor.serve_person()
        self.assertEqual(nombre, "Ana")
        self.assertEqual(tiempo, 5)

        nombre2, tiempo2 = gestor.serve_person()
        self.assertEqual(nombre2, "Luis")
        self.assertEqual(tiempo2, 3)

    # TODO: agrega más casos:
    # - atender_persona en cola vacía -> IndexError
    def test_atender_cola_vacia(self):
        gestor = QueueManager()
        with self.assertRaises(IndexError):
            gestor.serve_person()

    # - estado() refleja el orden actual
    def test_orden_actual(self):
        gestor = QueueManager()
        gestor.add_person("Ana", 5)
        gestor.add_person("Luis", 3)
        gestor.add_person("Sofía", 4)
        self.assertEqual(gestor.state(), ["Ana", "Luis", "Sofía"])

        gestor.serve_person()  # Atiende a Ana
        self.assertEqual(gestor.state(), ["Luis", "Sofía"])
        
    # - mezcla de agregar/atender repetidas veces
    def test_mezcla_operaciones(self):
        gestor = QueueManager()
        gestor.add_person("Ana", 5)
        gestor.add_person("Luis", 3)
        gestor.serve_person()  # Ana sale
        gestor.add_person("Sofía", 4)
        gestor.add_person("Carlos", 2)

        self.assertEqual(gestor.state(), ["Luis", "Sofía", "Carlos"])
        nombre, tiempo = gestor.serve_person()
        self.assertEqual(nombre, "Luis")
        self.assertEqual(tiempo, 3)
        self.assertEqual(gestor.state(), ["Sofía", "Carlos"])

if __name__ == "__main__":
    unittest.main()
