from models.user_admins_model import UserAdminModel, UserPersonalInfoModel
import traceback


class UsersSeeds:
    users = [
        {
            "first_name": "José",
            "last_name": "Orozco",
            "email": "jose.orozco@example.com",
            "phone_number": "123456789",
            "address": "123 Main St, Hometown",
            "date_of_birth": "1990-01-01T00:00:00",
            "user_admin": {"username": "orozcoDev", "password": "123456789"},
        },
        {
            "first_name": "Hawkins",
            "last_name": "Dev",
            "email": "hawkins.dev@example.com",
            "phone_number": "987654321",
            "address": "456 Elm St, Techie",
            "date_of_birth": "1985-05-15T00:00:00",
            "user_admin": {"username": "hawkinsDev", "password": "123456789"}
        }
    ]

    @classmethod
    def seed_user_admin(cls, session, user_admin) -> UserAdminModel:
        try:
            exits = session.query(UserAdminModel).filter_by(username=user_admin['username']).first()
            if not exits:
                row = UserAdminModel(**user_admin)
                session.add(row)
                session.flush()
                return row
            return exits
        except Exception as e:
            print(f'Ha ocurrido un error en la función seed_user_admin {e}')
            raise e

    @classmethod
    def seed_users(cls, session):
        try:
            users = cls.users
            all_exists = []
            for user in users:
                exits = session.query(UserPersonalInfoModel).filter(UserPersonalInfoModel.email == user['email']).first()
                if exits:
                    all_exists.append(exits.as_dict())
                    continue

                admin = cls.seed_user_admin(session, user["user_admin"])
                user.pop('user_admin')
                new_user = UserPersonalInfoModel(**user, id_user_admin=admin.id)
                session.add(new_user)
                session.commit()

            return exits
        except Exception as e:
            traceback.print_exc()
            print(f'Ha ocurrido un error en la función seed_user {e}')
            session.rollback()
