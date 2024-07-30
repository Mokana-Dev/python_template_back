from utils.database import Database
from seeds.example_seed import UsersAdminSeeds


class MainSeeds:

    @classmethod
    def main(cls):
        try:
            db = Database()
            session = db.get_session()

            UsersAdminSeeds.seed_users_admin(session)
        except Exception as e:
            print(f'Ha ocurrido un error en el MainSeeds {e}')


if __name__ == '__main__':
    MainSeeds.main()
