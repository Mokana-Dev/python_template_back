import os
import jwt
from datetime import datetime, timedelta
from schemas.auth.login_schema import AccessTokenSchema
from dotenv import load_dotenv
load_dotenv()


class Login:

    expired_minutes = int(os.getenv('ACCESS_TOKEN_EXPIRED_MINUTES'))
    secret_key = os.getenv('SECRET_KEY')
    algorithm = os.getenv('ALGORITHM_HASH')

    @classmethod
    def create_access_token(cls, data: dict) -> AccessTokenSchema:
        try:

            to_encode = data.copy()
            expired = datetime.utcnow() + timedelta(minutes=cls.expired_minutes)
            to_encode.update({"exp": expired})
            encode_jwt = jwt.encode(to_encode, cls.secret_key, cls.algorithm)
            return AccessTokenSchema(access_token=encode_jwt, expired=str(expired))
        except Exception as e:
            raise e

    @classmethod
    def verify_access_token(cls, token: str) -> bool:
        try:
            decode_jwt = jwt.decode(token, cls.secret_key, cls.algorithm)
            username: str = decode_jwt.get('sub')
            if username:
                return True
            return False
        except Exception as e:
            raise e

    @classmethod
    def logout(cls, token: str) -> bool:
        try:
            decode_jwt = jwt.decode(token, cls.secret_key, cls.algorithm)
            decode_jwt['exp'] = datetime.utcnow() - timedelta(minutes=cls.expired_minutes)
            jwt.encode(decode_jwt, cls.secret_key, cls.algorithm)
            return True
        except Exception as e:
            raise e
