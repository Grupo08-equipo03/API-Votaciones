from Repositorios.RepositorioVoto import RepositorioVoto
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioPartido import RepositorioPartido

class ControladorReportes():
    def __init__(self):
        self.repositorioVoto = RepositorioVoto()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioPartido = RepositorioPartido()
    
    # Contar Votos
    def contarVotos(self):
        return self.repositorioVoto.countDocuments()

