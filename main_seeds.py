from utils.database import Database
from seeds.users_seed import UsersSeeds


class MainSeeds:

    @classmethod
    def main(cls):
        try:
            db = Database()
            session = db.get_session()

            UsersSeeds.seed_users(session)
        except Exception as e:
            print(f'Ha ocurrido un error en el MainSeeds {e}')


if __name__ == '__main__':
    MainSeeds.main()
