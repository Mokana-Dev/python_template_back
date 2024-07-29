from models.example_model import ExampleModel


class ExampleSeeds:

    @classmethod
    def seed_programs(cls, session):
        try:
            programs = [
                {"name": "Bill payment", "description": "BOT para pagar facturas."},
                {"name": "Credit store", "description": "BOT para ofrecer creditos a tiendas."}
            ]

            for program in programs:
                exits = session.query(ExampleModel).filter_by(name=program['name']).first()
                if not exits:
                    prog = ExampleModel(**program)
                    session.add(prog)

            session.commit()
        except Exception as e:
            print(f'Ha ocurrido un error en la función seed_programs {e}')
