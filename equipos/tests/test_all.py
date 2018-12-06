from django.test import TestCase
from equipos.models import Equipo

class TestViewEliminar(TestCase):

    def test_eliminar_equipo_existente(self):
        self.assertEquals(Equipo.objects.count(), 1)
        id = str(self.equipo.id)
        response = self.client.get('equipos/eliminar/lista'+id)
        self.assertEquals(Equipo.objects.count(), 0)
        

    def test_eliminar_equipo_no_existente(self):
        self.assertEquals(Equipo.objects.count(), 1)
        data = {'id_equipo':self.equipo.id+1}
        response = self.client.post('equipos/eliminar/lista', data=data)
        self.assertEqual(response.context['error'], "No se encuentra el equipo en la lista")
