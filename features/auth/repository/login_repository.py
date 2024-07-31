from utils.database import Database
from models.user_admins_model import UserAdminModel
from sqlalchemy import and_


class LoginRepository:
    def __init__(self):
        self.db = Database()
        self.session = self.db.get_session()

    def get_user(self, username: str) -> UserAdminModel:
        user = self.session.query(UserAdminModel).filter(and_(
            UserAdminModel.username == username,
            UserAdminModel.active == 1)
            ).first()
        self.session.close()
        return user
