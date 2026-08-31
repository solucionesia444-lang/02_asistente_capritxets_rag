from pydantic import BaseModel, Field


class RagRequest(BaseModel):
    query: str = Field(min_length=1, pattern=r".*\S.*")