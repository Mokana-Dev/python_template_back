from utils.model_response import ModelResponse
from schemas.auth.login_schema import LoginSchema
from features.auth.repository.login_repository import LoginRepository
from features.auth.Class.login import Login


class LoginService(ModelResponse):
    def __init__(self):
        self.login_repository = LoginRepository()

    def login(self, payload: LoginSchema):
        try:
            username = payload.username
            password = payload.password

            user = self.login_repository.get_user(username)
            if user is None:
                return self.not_found('user no found')

            if user.password != password:
                return self.bad_request("incorrect username or password")

            access = Login.create_access_token({'sub': username})
            return self.success(access.model_dump())
        except ValueError as e:
            print(f'error to login {e}')
            raise e
        except Exception as e:
            print(f'error to login {e}')
            raise e

    def logout(self, token: str):
        try:
            logout = Login.logout(token)
            return self.success(logout)
        except ValueError as e:
            print(f'error to login {e}')
            raise e
        except Exception as e:
            print(f'error to login {e}')
            raise e
