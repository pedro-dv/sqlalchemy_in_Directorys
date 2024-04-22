from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = 'mysql+pymysql://root:@localhost:3306/cinema'
        self.__engine = self.__creante_database_engine()
        self.session = None

    def __creante_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine



            # <--- entrando na sessao e fechando -->
    def __enter__(self):
        session_Maker = sessionmaker(bind=self.__engine)
        self.session = session_Maker()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()



