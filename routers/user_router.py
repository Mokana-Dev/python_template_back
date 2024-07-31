from fastapi import APIRouter, Depends
from utils.jwt_bearer import JWTBearer
from features.users.services.user_service import UserService
from schemas.user.user_schema import CreateUserPersonalInfoSchema, UserAdminSchema


User_router = APIRouter(
    prefix="/users",
    tags=['Users'],
    dependencies=[Depends(JWTBearer())]
)
User_service = UserService()


@User_router.post(
    path="/create",
    summary="Creación de User.",
    response_model=CreateUserPersonalInfoSchema
)
def createUser(payload: CreateUserPersonalInfoSchema):
    user = User_service.create(payload)
    return user


@User_router.post(
    path="/admin",
    summary="Creación de user admin.",
    response_model=UserAdminSchema
)
def createUserAdmin(payload: UserAdminSchema):
    create_user_admin = User_service.createUserAdmin(payload)
    return create_user_admin
