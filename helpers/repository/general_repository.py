from sqlalchemy.ext.declarative import DeclarativeMeta
from pydantic import BaseModel
from typing import List, TypeVar, Type
from sqlalchemy.orm import Session
from .interface import IRepository
from sqlalchemy import and_, sql

T = TypeVar('T', bound=BaseModel)
Model = TypeVar('Model')


class SQLAlchemyRepository(IRepository[T]):
    def __init__(self, model: Type[Model], session: Session):
        self.model = model
        self.session = session

    def refresh_db(self, model_obj: DeclarativeMeta):
        self.session.add(model_obj)
        self.session.commit()
        self.session.refresh(model_obj)
        self.session.close()

    def get_by_id(self,  id: int) -> Model:
        return self.session.query(self.model).filter(and_(self.model.id == id, self.model.active == 1)).first()

    def get_all(self) -> List[Model]:
        return self.session.query(self.model).filter(self.model.active == 1).all()

    def find(self, options: T) -> List[Model]:
        filter_options = options.model_dump(exclude_none=True)
        filters = []

        for field, value in filter_options.items():
            attr = getattr(self.model, field, None)
            filters.append(attr == value)

        payload_query = self.session.query(self.model)
        if filters:
            payload_query = payload_query.filter(and_(*filters))

        return payload_query.all()

    def create(self, entity: T) -> Model:
        row = self.model(**entity.model_dump())
        self.refresh_db(row, self.session)
        return row

    def update(self, id: int, entity: T) -> Model:
        row = self.get_by_id(id)

        if row is None:
            return None

        entity_dict = entity.model_dump(exclude_none=True)

        for field, value in entity_dict.items():
            setattr(row, field, value)

        setattr(row, 'updated_at', sql.func.now())

        self.refresh_db(row)
        return row

    def delete(self, id: int) -> None:
        row = self.get_by_id(id)

        if row is None:
            return None

        setattr(row, 'active', 0)
        setattr(row, 'updated_at', sql.func.now())

        self.refresh_db(row)
        return row

    def paginate(self, page: int, page_size: int) -> List[Model]:
        return self.session.query(self.model).offset(page * page_size).limit(page_size).all()
