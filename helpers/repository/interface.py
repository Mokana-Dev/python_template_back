from typing import Generic, TypeVar, List, Optional

T = TypeVar('T')


class IRepository(Generic[T]):

    def get_by_id(self, id) -> T:
        raise NotImplementedError

    def get_all(self) -> List[T]:
        raise NotImplementedError

    def find(self, entity: T) -> Optional[T]:
        raise NotImplementedError

    def create(self, entity: T) -> T:
        raise NotImplementedError

    def update(self, id: int, entity: T) -> T:
        raise NotImplementedError

    def delete(self, id: int) -> T:
        raise NotImplementedError

    def paginate(self, page: int, page_size: int) -> T:
        raise NotImplementedError
