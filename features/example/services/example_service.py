from utils.model_response import ModelResponse
from features.example.repository.example_repository import ExampleRepository


class ExampleService(ModelResponse):
    def __init__(self):
        self.program_repository = ExampleRepository()

    def get_program(self, id: int):
        try:
            program = self.program_repository.get_by_id(id)
            if program is None:
                return None

            return program.as_dict()
        except ValueError as e:
            print(f'error to get_program {e}')
            raise e
        except Exception as e:
            print(f'error to get_program {e}')
            raise e

    def get_all_program(self):
        try:
            programs = self.program_repository.get_all()
            return [program.as_dict() for program in programs]
        except ValueError as e:
            print(f'error to get_all_programs {e}')
            raise e
        except Exception as e:
            print(f'error to get_all_programs {e}')
            raise e

    def create_program(self, program: any):
        try:
            program_db = self.program_repository.create(program)

            if program_db is None:
                return None

            return program_db.as_dict()
        except ValueError as e:
            print(f'error to crate program {e}')
            raise e
        except Exception as e:
            print(f'error to create program {e}')
            raise e

    def update_program(self, id: int,  program: any):
        try:
            program_db = self.program_repository.update(id, program)

            if program_db is None:
                return None

            return program_db.as_dict()
        except ValueError as e:
            print(f'error to update program {e}')
            raise e
        except Exception as e:
            print(f'error to update program {e}')
            raise e

    def delete_program(self, id: int):
        try:
            program_db = self.program_repository.deactivate(id)

            if program_db is None:
                return None

            return program_db.as_dict()
        except ValueError as e:
            print(f'error to delete program {e}')
            raise e
        except Exception as e:
            print(f'error to delete program {e}')
            raise e
