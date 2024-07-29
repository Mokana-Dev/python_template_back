from schemas.example.example_schema import ExampleCreateSchema, ExampleUpdateSchema
from utils.database import Database
from models.example_model import ExampleModel
from sqlalchemy import and_, sql


class ExampleRepository:
    def __init__(self):
        self.db = Database()
        self.session = self.db.get_session()

    def refresh_db(self, object_model):
        self.session.add(object_model)
        self.session.commit()
        self.session.refresh(object_model)

    def get_all(self):
        examples = self.session.query(ExampleModel).filter(ExampleModel.state == 1)
        self.session.close()
        return examples

    def get_by_id(self, id: int):
        example = self.session.query(ExampleModel).filter(and_(
            ExampleModel.id == id,
            ExampleModel.state == 1)
            ).first()
        self.session.close()
        return example

    def create(self, example: ExampleCreateSchema) -> ExampleCreateSchema:
        new_example = ExampleModel(**example.model_dump())
        self.session.add(new_example)
        self.refresh_db(new_example)
        self.session.close()
        return new_example

    def update(self, id: int, payload: ExampleUpdateSchema) -> ExampleUpdateSchema:
        get_example = self.get_by_id(id)
        example_dict = payload.model_dump()
        example_dict['date_update'] = sql.func.now()
        for key, value in example_dict.items():
            setattr(get_example, key, value)
        self.refresh_db(get_example)
        self.session.close()
        return get_example

    def delete(self, id: int):
        get_example = self.get_by_id(id)
        get_example.state = 0
        get_example.date_update = sql.func.now()
        self.refresh_db(get_example)
        self.session.close()
        return True
