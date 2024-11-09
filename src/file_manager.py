from abc import ABC, abstractmethod


class FileManager(ABC):
    """Абстрактный родительский класс для работы с json-файлом"""

    @abstractmethod
    def read_json_file(self):
        """Метод для чтения данных json-файла"""
        pass

    @abstractmethod
    def add_vacancy(self, *args, **kwargs):
        """Метод для добавления новых данных в json-файл"""
        pass

    @abstractmethod
    def delete_vacancy(self):
        """Метод удаления данных из json-файла"""
        pass
