from utils.model_response import ModelResponse
from schemas.user.user_schema import CreateUserPersonalInfoSchema, UserAdminSchema, UserFilterSchema
from features.users.repository.user_repository import UserRepository


class UserService(ModelResponse, UserRepository):

    def create(self, payload: CreateUserPersonalInfoSchema):
        try:
            filters = UserFilterSchema(email=payload.email)
            exits_user = self.sqlalchemy_repository.find(filters)
            if exits_user:
                return self.bad_request('email to exits.')

            new_user = self.create_user_info(payload)
            if new_user is None:
                return self.bad_request('error to created user.')

            return self.success(new_user.as_dict())
        except ValueError as e:
            print(f'error to create {e}')
            raise e
        except Exception as e:
            print(f'error to create {e}')
            raise e

    def createUserAdmin(self, payload: UserAdminSchema):
        try:
            new_user_admin = self.create_user_admin_temp(payload)
            if new_user_admin is None:
                return self.bad_request('error to created user admin.')
            return new_user_admin
        except ValueError as e:
            print(f'error to create {e}')
            raise e
        except Exception as e:
            print(f'error to create {e}')
            raise e
