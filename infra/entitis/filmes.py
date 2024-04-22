from infra.configs.base import base
from sqlalchemy import Column, String, Integer

class Filmes(base):
    __tablename__ = "filmes"
    titulo = Column(String, primary_key = True)
    genero = Column(String, nullable= False)
    ano = Column(Integer, nullable= False)

    def __repr__(self):
        return f'Filmes: [titulo: {self.titulo}, genero: {self.genero}, ano: {self.ano}]'




