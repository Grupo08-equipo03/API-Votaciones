from Repositorios.RepositorioCandidato import RepositorioCandidato
from Modelos.Candidato import Candidato


class ControladorCandidato():
    #init
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
    #findall
    def index(self):
        return self.repositorioCandidato.findAll()
    # create
    def create(self,informacionCandidato):
        nuevoCandidato=Candidato(informacionCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)
    #update
    def update(self,id,informacionCandidato):
        candidatoCambiar=Candidato(self.repositorioCandidato.findById(id))
        candidatoCambiar.resolucion=informacionCandidato["resolucion"]
        candidatoCambiar.cedula=informacionCandidato["cedula"]
        candidatoCambiar.nombre=informacionCandidato["nombre"]
        candidatoCambiar.apellido= informacionCandidato["apellido"]
        return self.repositorioCandidato.save(candidatoCambiar)
    #search
    def show(self,id):
        candidato=Candidato(self.repositorioCandidato.findById(id))
        return candidato.__dict__
    #delete
    def delete(self,id):
        return self.repositorioCandidato.delete(id)
    
