from typing import List, Optional
from pydantic import BaseModel, EmailStr

from user.models import UserRoleChoices

class UserDomainModel(BaseModel):
    email: Optional[EmailStr]
    name: Optional[str]
    username: Optional[str]
    address: Optional[str]
    role: Optional[UserRoleChoices]

    class Config:
        orm_mode: True

class UserListDomainModel(BaseModel):
    __root__ = [List[UserDomainModel]]

    def __iter__(self):
        return iter(self.root)

    def __len__(self):
        return len(self.root)

    def __getitem__(self, item):
        return self.root[item]