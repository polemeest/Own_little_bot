from pydantic import BaseModel
from enum import StrEnum

class UserRoleEnum(StrEnum):
    admin = "Admin"
    user = "User"


class ResolutionStatus(StrEnum):
    intro = "внесено"
    wip = "на рассмотрении"
    done = "принято решение"