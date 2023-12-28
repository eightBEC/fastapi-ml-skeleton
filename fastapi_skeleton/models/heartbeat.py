from pydantic import BaseModel


class HearbeatResult(BaseModel):
    is_alive: bool
