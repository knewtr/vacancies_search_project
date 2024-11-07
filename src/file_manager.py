from abc import ABC, abstractmethod


class FileManager(ABC):
    """Абстрактный родительский класс для работы с json-файлом"""

    def __init__(self, __file_worker):
        self.file_worker = __file_worker

    @abstractmethod
    def read_json_file(self, *args):
        """Метод для чтения данных json-файла"""
        pass

    @abstractmethod
    def add_vacancy(self, *args, **kwargs):
        """Метод для добавления новых данных в json-файл"""
        pass

    @abstractmethod
    def delete_vacancy(self, *args, **kwargs):
        """Метод удаления данных из json-файла"""
        pass
