from models.user_admins_model import UserAdminModel


class UsersAdminSeeds:

    @classmethod
    def seed_users_admin(cls, session):
        try:
            users = [
                {"username": "hawkinsDev", "password": "221122"},
                {"username": "orozcoDev", "password": "123456789"}
            ]

            for user in users:
                exits = session.query(UserAdminModel).filter_by(username=user['username']).first()
                if not exits:
                    prog = UserAdminModel(**user)
                    session.add(prog)

            session.commit()
        except Exception as e:
            print(f'Ha ocurrido un error en la función seed_users {e}')
