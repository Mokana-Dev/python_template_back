# database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy_utils import database_exists, create_database
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()


class Database:
    _instance = None

    def __new__(cls):
        try:
            if cls._instance is None:
                cls._instance = super(Database, cls).__new__(cls)
                cls._instance.engine = create_engine(cls.__get_connection_strings())
                if not database_exists(cls._instance.engine.url):
                    create_database(cls._instance.engine.url)
                cls._instance.Session = sessionmaker(bind=cls._instance.engine)
            return cls._instance
        except Exception as e:
            print(f"error connect to database {e}")

    def get_session(self):
        return self.Session()

    @classmethod
    def __get_connection_strings(cls, credentials_data=None):
        """
        Si el nombre de la base de datos no está vacío, devuelva la cadena de conexión con el nombre de
        la base de datos; de lo contrario, devuelva la cadena de conexión con el nombre de la base de
        datos predeterminado

        :param credentials_data:
        :return: La cadena de conexión
        """
        user = os.getenv('USER_DB')
        password = os.getenv('PASSWORD_DB')
        host = os.getenv('SERVER_DB')
        db_name = os.getenv('NAME_DB')

        string_conexion = f"mysql+pymysql://{user}:{password}@{host}/{db_name}"
        # Se retorna la cadena de conexión
        return string_conexion
