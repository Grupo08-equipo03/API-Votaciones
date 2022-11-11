from Modelos.Voto import Voto
from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa
from Repositorios.RepositorioVoto import RepositorioVoto
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesa import RepositorioMesa

class ControladorVoto():
    def __init__(self):
        self.repositorioVoto = RepositorioVoto()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioMesa = RepositorioMesa()

    # Listar todos los votos
    def index(self):
        return self.repositorioVoto.findAll()
    
    # Asignacion de un candidato y mesa (a la mesa se le asigna un partido politico) a voto / resultado
    def create(self, infoVoto, id_candidato, id_mesa):
        nuevoVoto = Voto(infoVoto)
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        nuevoVoto.candidato = elCandidato
        nuevoVoto.mesa = laMesa
        return self.repositorioVoto.save(nuevoVoto)

    # Buscar voto por id
    def show(self, id):
        elVoto = Voto(self.repositorioVoto.findById(id))
        return elVoto.__dict__
    
    # Modificación de voto  (si se va a permitir) (candidato y mesa)
    # def update(self, id, infoVoto, id_candidato, id_mesa):
    #     elVoto = Voto(self.repositorioVoto.findById(id))
    #     elVoto.fecha = infoVoto['fecha']
    #     elVoto.candidato = infoVoto["candidato"]
    #     elVoto.mesa = infoVoto["mesa"]
    #     elCandidato = Candidato(self.repositorioVoto.findById(id_candidato))
    #     laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
    #     elVoto.candidato = elCandidato
    #     elVoto.mesa = laMesa
    #     return self.repositorioVoto.save(elVoto)
    
    # Eliminar voto (si se va a permitir)
    def delete(self, id):
        return self.repositorioVoto.delete(id)