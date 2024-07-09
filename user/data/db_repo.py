from user.data.abstract_repo import UserAbstractRepository
from user.domain.domain_models import UserDomainModel, UserListDomainModel
from user.models import User

class UserDbRepository(UserAbstractRepository):
    """User database repository."""

    def bulk_get(self) -> UserListDomainModel:
        """Get all user"""
        user_db_entries = User.objects.all()
        return UserListDomainModel(
            __root__=list(map(
                UserDomainModel.from_orm,
                user_db_entries
            ))
        )
