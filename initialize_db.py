# initialize_db.py
from utils.database import Database, Base
from models.example_model import ExampleModel # noqa F401


def initialize_db():
    db = Database()
    Base.metadata.create_all(bind=db.engine)
    print("la creación de las tablas a sido exitosa.")


if __name__ == "__main__":
    initialize_db()
