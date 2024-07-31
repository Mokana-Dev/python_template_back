from sqlalchemy import Column, Integer, String, sql, DateTime, text, ForeignKey, Date
from sqlalchemy.orm import relationship
from utils.model_response import ModelResponse
from utils.database import Base


class UserAdminModel(Base):
    __tablename__ = 'users_admins'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), nullable=False)
    password = Column(String(50), nullable=False)
    active = Column(Integer, server_default=text('1'))
    last_date_login = Column(DateTime, nullable=True)
    date_created = Column(DateTime, nullable=False, server_default=sql.func.now())
    date_update = Column(DateTime, nullable=True)

    def as_dict(self):
        return ModelResponse.to_dict(self)


class UserPersonalInfoModel(Base):
    __tablename__ = 'users_personal_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone_number = Column(String(15), nullable=True)
    address = Column(String(200), nullable=True)
    date_of_birth = Column(Date, nullable=True)
    active = Column(Integer, server_default=text('1'))
    date_created = Column(DateTime, nullable=False, server_default=sql.func.now())
    date_updated = Column(DateTime, nullable=True)
    id_user_admin = Column(Integer, ForeignKey('users_admins.id'))
    user_admin = relationship('UserAdminModel', lazy='joined')

    def as_dict(self):
        return ModelResponse.to_dict(self, True)
