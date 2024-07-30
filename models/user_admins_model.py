from sqlalchemy import Column, Integer, String, sql, DateTime, text
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
