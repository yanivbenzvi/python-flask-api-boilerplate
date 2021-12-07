import uuid

from src.utility import MemoryDbStore


class EntityModel:
    """
    Entity model
    """

    def __init__(self):
        self.id = uuid.uuid4()

    def __str__(self):
        return str(self.id)

    def to_json(self):
        return {
            'id': str(self.id),
        }

    @staticmethod
    def get(entity_id: str):
        """
        Returns a user from the database
        :param entity_id: str
        :return: User
        """

        entity_object = MemoryDbStore().get(entity_id)

        return entity_object if entity_object else None

    def save(self):
        MemoryDbStore().set(str(self.id), self)

    def delete(self):
        MemoryDbStore().delete(str(self.id))

    @classmethod
    def get_all(cls):
        """
        Returns a list of all users in the database
        :return: list[User]
        """
        return MemoryDbStore().get_all_by_instance_type(cls)
