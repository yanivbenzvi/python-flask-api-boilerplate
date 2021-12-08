from copy import deepcopy


class MemoryDbStore:
    """
    Singleton instance of in memory db

    """
    __instance = None
    __db = {}

    def __new__(cls):
        """
        Singleton implementation
        """
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def get(self, key):
        """
        Get an item from the db by his key
        :param key:
        :return:
        """
        return deepcopy(self.__db.get(key, None))

    def get_all_by_instance_type(self, instance_type):
        """
        Get all instances of a given type
        :param instance_type:
        :return: list of instances
        """
        return [item for item in self.__db.values() if isinstance(item, instance_type)]

    def set(self, key, value):
        """
        Set an item in the db by his key and value
        :param key:
        :param value:
        :return:
        """
        self.__db[key] = value

    def delete(self, key):
        """
        Delete an item from the db by his key
        :param key:
        :return:
        """
        del self.__db[key]

    def clear(self):
        """
        Clear the db
        :return:
        """
        self.__db.clear()
