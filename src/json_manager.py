import json
import os

from src.file_manager import FileManager
from src.vacancy import Vacancy


class JSONSaver(FileManager):
    """Класс для работы с JSON-файлами"""

    def __init__(self, file_worker="data/vacancies.json"):
        self.__file_worker = file_worker
        try:
            with open(self.__file_worker, encoding="utf-8") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("Файл не существует")

    def read_json_file(self):
        """Метод для чтения данных json-файла"""
        if self.__file_worker:
            with open(self.__file_worker, "r", encoding="utf-8") as file:
                data = json.load(file)
            return data
        else:
            return []

    def add_vacancy(self, vacancy: Vacancy):
        """Метод для добавления новых данных в json-файл"""
        vacancy_dict = Vacancy.vacancy_dict
        with open(self.__file_worker, "a", encoding='utf-8') as file:
            data = json.load(file)
            json.dump(vacancy_dict, file)

    def delete_vacancy(self):
        """Метод удаления данных из json-файла"""
        with open(self.__file_worker, "w") as file:
            data = json.load(file)
            json.dump(data, file)


# if __name__ == "__main__":
#     vac_1 = Vacancy.new_vacancy({"name": 'test1', "url": "test1", "salary": 1, "description": "test1"})
#     print(JSONSaver().read_json_file)
#     JSONSaver().add_vacancy(vac_1)
