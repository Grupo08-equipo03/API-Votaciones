from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Mesa import Mesa
from Modelos.Partido import Partido
class ControladorMesa():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()
        self.repositorioPartido = RepositorioPartido()
    def index(self):
        return self.repositorioMesa.findAll()
    def create(self,infoMesa):
        nuevoMesa=Mesa(infoMesa)
        return self.repositorioMesa.save(nuevoMesa)
    def show(self,id):
        elMesa=Mesa(self.repositorioMesa.findById(id))
        return elMesa.__dict__
    def update(self,id,infoMesa):
        mesaActual=Mesa(self.repositorioMesa.findById(id))
        mesaActual.cedula=infoMesa["cedula"]
        return self.repositorioMesa.save(mesaActual)
    def delete(self,id):
        return self.repositorioMesa.delete(id)
    """
    Relación partido y mesa
    """
    def asignarPartido(self, id, id_partido):
        mesaActual = Mesa(self.repositorioMesa.findById(id))
        partidoActual = Partido(self.repositorioPartido.findById(id_partido))
        mesaActual.partido = partidoActual
        return self.repositorioMesa.save(mesaActual)