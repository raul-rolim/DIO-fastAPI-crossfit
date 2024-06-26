from pydantic import Field
from sqlalchemy.sql.annotation import Annotated
from workout_api.contrib.schemas import BaseSchema


class Categoria(BaseSchema):
    nome: Annotated[str, Field(description='Nome da categoria',
                              examples='Scale',
                              max_length=10)]
