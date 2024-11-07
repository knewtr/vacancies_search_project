import json
import os

from src.file_manager import FileManager
from src.vacancy import Vacancy


class JSONSaver(FileManager):
    def __init__(self, file_worker=os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "vacancies.json")):
        self.__file_worker = file_worker
        try:
            with open(self.__file_worker, encoding="utf-8") as file:
                data = json.load(file)
                self.exist = True
        except FileNotFoundError:
            print("Файл не существует")
            self.exist = False

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
        vacancy_dict = vacancy.vacancy_dict
        if not self.exist:
            with open(self.__file_worker, "w") as file:
                self.exist = True
                add_data_vacancy = [vacancy_dict]
                json.dump(add_data_vacancy, file)
        else:
            data = self.read_json_file()

    def delete_vacancy(self):
        """Метод удаления данных из json-файла"""
        with open(self.__file_worker, "w") as file:
            data = json.load(file)
            json.dump(data, file)
            self.exist = True
