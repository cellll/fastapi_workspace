from datetime import datetime
from typing import Union, List, Dict

from fastapi import Form, APIRouter, Depends, HTTPException, File, UploadFile
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates
from sse_starlette.sse import EventSourceResponse

from models.sample_model import SampleBody

router = APIRouter(prefix='/api/v2', tags=['api', 'v2'])
templates = Jinja2Templates(directory='templates')
RETRY_TIMEOUT = 30000

# @router.put('')
# @router.delete('')
# @router.get('')
@router.post('/test')
async def test(request: Request, body: SampleBody) -> dict:
    # do something
    return request.app.main.sample_method(body)

