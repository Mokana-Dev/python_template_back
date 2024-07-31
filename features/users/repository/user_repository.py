from utils.database import Database
from models.user_admins_model import UserAdminModel, UserPersonalInfoModel
from helpers.repository.general_repository import SQLAlchemyRepository
from schemas.user.user_schema import UserAdminSchema, CreateUserPersonalInfoSchema
import traceback


class UserRepository:
    def __init__(self):
        self.db = Database()
        self.session = self.db.get_session()
        self.sqlalchemy_repository = SQLAlchemyRepository(UserPersonalInfoModel, self.session)

    def create_user_admin_temp(self, payload: UserAdminSchema):
        row = UserAdminModel(**payload.model_dump())
        self.session.add(row)
        self.session.flush()
        return row

    def create_user_info(self, payload: CreateUserPersonalInfoSchema):
        try:
            admin = self.create_user_admin_temp(payload.user_admin)

            payload_dict = payload.model_dump()
            payload_dict.pop('user_admin')

            new_user = UserPersonalInfoModel(**payload_dict, id_user_admin=admin.id)
            self.session.add(new_user)
            self.session.commit()

            return new_user
        except Exception:
            traceback.print_exc()
            self.session.rollback()
