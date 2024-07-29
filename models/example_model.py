from sqlalchemy import Column, Integer, String, ForeignKey, sql, DateTime, text
from sqlalchemy.orm import relationship
from utils.model_response import ModelResponse
from utils.database import Base


class ExampleModel(Base):
    __tablename__ = 'table_example'

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(20), nullable=False)
    name = Column(String(50), nullable=False)
    description = Column(String(250), nullable=False)
    price = Column(String(10), nullable=False)
    state = Column(Integer, server_default=text('1'))
    date_created = Column(DateTime, nullable=False, server_default=sql.func.now())
    date_update = Column(DateTime, nullable=True)
    id_example_user_type = Column(Integer, ForeignKey('examples_users_type.id'))
    example_user_type = relationship('exampleUserTypeModel', lazy='joined')
    example_attributes = relationship('AttributesForExampleModel', lazy='joined')

    def as_dict(self):
        return ModelResponse.to_dict(self, True)
