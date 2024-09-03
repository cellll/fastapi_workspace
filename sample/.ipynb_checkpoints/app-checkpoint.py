import os
import logging
import uvicorn

from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from router.sample_router import router as sample_router
from internal.main import MainClass

# app
app = FastAPI()
dirpath = os.path.dirname(os.path.realpath(__file__))
app.mount('/static', StaticFiles(directory=os.path.join(dirpath, 'statics')), name='static')

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://0.0.0.0", 
    "http://0.0.0.0:8000", 
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.main = MainClass()
app.include_router(router=sample_router)

# exception handler 
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
    print (f"{request}: {exc_str}")
    content = {'status_code': 10422, 'message': exc_str, 'data': None}
    return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)

if __name__ == '__main__':
    uvicorn.run('app:app', host=_HOST, port=_PORT, reload=True)