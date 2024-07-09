import abc
from typing import List

from user.domain.domain_models import UserListDomainModel

class UserAbstractRepository(abc.ABC):
    """User abstract repository."""

    @abc.abstractmethod
    def bulk_get(self) -> UserListDomainModel:
        """Get all user"""
