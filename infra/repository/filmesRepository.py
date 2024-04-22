from infra.configs.connection import DBConnectionHandler
from infra.entitis.filmes import Filmes


class Filmes_Repository:

    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Filmes).all()
            return data

    def insert(self, titulo, genero, ano):
        with DBConnectionHandler() as db:
            data_insert = Filmes(titulo=titulo, genero=genero, ano=ano)
            db.session.add(data_insert)
            db.session.commit()


    def delete(self, titulo):
        with DBConnectionHandler() as db:
            db.session.query(Filmes).filter(Filmes.titulo == titulo).delete()
            db.session.commit()

    def update(self, titulo, ano):
        with DBConnectionHandler() as db:
            db.session.query(Filmes).filter(Filmes.titulo == titulo).update({'ano': ano})
            db.session.commit()

