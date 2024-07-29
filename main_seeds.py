from utils.database import Database
from seeds.example_seed import ExampleSeeds


class MainSeeds:

    @classmethod
    def main(cls):
        try:
            db = Database()
            session = db.get_session()

            ExampleSeeds.seed_programs(session)
        except Exception as e:
            print(f'Ha ocurrido un error en el MainSeeds {e}')


if __name__ == '__main__':
    MainSeeds.main()
