from pydantic import BaseModel
import json


class News(BaseModel):
    headline: str
    link: str
    source: str

    def to_json(self):
        return json.dumps(self, default=lambda c: c.__dict__, indent=4)
