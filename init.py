from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from routers.list_routers import list_routers
from fastapi.exceptions import RequestValidationError
from utils.model_response import ModelResponse

app = FastAPI()

origins = ['*']

for router in list_routers:
    app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return ModelResponse.validation_error(exc)


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    return ModelResponse.internal_server_error()


@app.exception_handler(ValueError)
async def value_error_handler(request: Request, exc: ValueError):
    return ModelResponse.internal_server_error()


@app.get("/", tags=["Welcome"])
def welcome():
    return {"message": "welcome to backend python ⚓."}
