import unittest
from features.example.repository.example_repository import ExampleRepository
from schemas.example.example_schema import ExampleCreateSchema


class test_example_repository(unittest.TestCase):
    def test_example_repository(self):
        new_example = ExampleCreateSchema(name='Jose', description='nada que decir')
        response_repository = ExampleRepository().create(new_example)
        self.assertEqual(response_repository.name, 'Jose')
        self.assertEqual(response_repository.description, 'nada que decir')


if __name__ == "__main__":
    unittest.main()
