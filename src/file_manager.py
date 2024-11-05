from abc import ABC, abstractmethod

class FileManager(ABC):
    """Абстрактный родительский класс для работы с json-файлом"""
    def __init__(self, _file_worker):
        self.file_worker = _file_worker #путь к файлу, с которым мы будем работать, а именно, сохранять, добавлять, удалять вакансии

    @abstractmethod
    def read_json_file(self, *args):
        """Метод для чтения и возврата данных json-файла"""
        pass

    @abstractmethod
    def add_to_json_file(self, *args, **kwargs):
        """Метод для добавления новых данных в json-файл"""
        pass

    @abstractmethod
    def delete_vacancy(self, *args, **kwargs):
        pass
