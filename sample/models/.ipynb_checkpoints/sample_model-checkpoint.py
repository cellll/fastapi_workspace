import datetime
from typing import List, Optional, Tuple
from pydantic import BaseModel, BaseSettings, Field

from models.sample_model import SampleBody

class SampleBody(BaseModel):
    sample_id: int
    sample_data: str = Field(default='', description='sample string data')
    sample_data_list: List[str] = Field(default=[], description='sample string data list')

    