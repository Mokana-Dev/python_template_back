from fastapi import APIRouter
# from utils.jwt_bearer import JWTBearer
from features.auth.services.login_service import LoginService
from schemas.auth.login_schema import LoginSchema, AccessTokenSchema


login_router = APIRouter(
    prefix="/auth",
    tags=['Authentication'],
    # dependencies=[Depends(JWTBearer())]
)
login_service = LoginService()


@login_router.post(
    path="/login",
    summary="Autenticación de login.",
    response_model=AccessTokenSchema
)
def login(payload: LoginSchema):
    user = login_service.login(payload)
    return user


@login_router.post(
    path="/logout/{token}",
    summary="Autenticación de logout.",
    response_model=AccessTokenSchema
)
def logout(token: str):
    logout_user = login_service.logout(token)
    return logout_user
