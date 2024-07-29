from fastapi import APIRouter
from schemas.example.example_schema import ExampleCreateSchema, ExampleUpdateSchema
from utils.model_response import ModelResponse
from features.example.repository.example_repository import ExampleRepository
# from utils.jwt_bearer import JWTBearer

repo_Examples = ExampleRepository()

Example_router = APIRouter(
    # dependencies=[Depends(JWTBearer())],
    prefix='/Examples',
    tags=['Examples'],
    # route_class=CustomValidationError
)


@Example_router.get(
    path='/',
    summary='Obtiene todas las membresías',
    description='Obtiene todas las membresías disponibles para los usuarios Entrenado, GYM'
)
def get_all():
    Examples = repo_Examples.get_all()
    return ModelResponse.success(Examples, message='Obtienes todas las membresías')


@Example_router.get(
    path='/{id}',
    summary='Obtiene una membresía',
    description='Obtiene una membresía para el usuario Entrenado o GYM',
)
def get_by_id(id: int):
    Example = repo_Examples.get_by_id(id)
    return ModelResponse.success(Example)


@Example_router.post(
    path='/',
    summary='Crea una membresía',
    description='Crea la membresía para el usuario Entrenado o GYM',
)
def create(payload: ExampleCreateSchema):
    Examples = repo_Examples.create(payload)
    return ModelResponse.success_create(Examples)


@Example_router.put(
    path='/{id}',
    summary='Actualiza una membresía',
    description='Actualiza la membresía para el usuario tipo Entrenador o GYM',
)
def update(id, payload: ExampleUpdateSchema):
    Examples = repo_Examples.update(id, payload)
    return ModelResponse.success(Examples, 'Actualización exitosa.')


@Example_router.delete(
    path='/{id}',
    summary='elimina una membresía',
    description='elimina la membresía de un usuario tipo Entrenador o GYM',
)
def delete(id: int):
    Examples = repo_Examples.delete(id)
    print('entre al endpoint')
    return ModelResponse.success(Examples, 'Eliminación exitosa.')
