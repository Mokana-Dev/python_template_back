from typing import Callable
from fastapi.responses import JSONResponse
from fastapi.routing import APIRoute
from fastapi.exceptions import RequestValidationError
from utils.model_response import ModelResponse


class CustomValidationError(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request) -> JSONResponse:
            try:
                return await original_route_handler(request)
            except RequestValidationError as ex:
                return ModelResponse.validation_error(ex)
            except Exception as e:
                print(f'No se pudo consumir el servicio: {e.message}')
                return ModelResponse.internal_server_error()

        return custom_route_handler
