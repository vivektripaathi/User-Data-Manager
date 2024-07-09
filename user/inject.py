from dependency_injector import containers, providers

from user.data.db_repo import UserDbRepository
from user.data.abstract_repo import UserAbstractRepository

class UserContainer(containers.DeclarativeContainer):
    db_repo = providers.Dependency(
        instance_of=UserAbstractRepository,
        default=UserDbRepository(),
    )