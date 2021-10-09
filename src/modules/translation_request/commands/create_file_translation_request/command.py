from pydantic import BaseModel
from typing import Union
from sanic.request import File

class CreateFileTranslationRequestCommand(BaseModel):
    
    source_file: File
    source_lang: Union[str, None]
    target_lang: str

    class Config:
        arbitrary_types_allowed = True
