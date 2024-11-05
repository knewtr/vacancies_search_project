import json
import os


from src.file_manager import FileManager
from src.vacancy import Vacancy

file_path  = os.path.join(os.path.dirname(os.path.dirname(__file__)), "vacancies.json")

class JSONSaver(FileManager):
    def __init__(self, _file_worker):
        super().__init__(_file_worker)

    def read_json_file(self, _file_worker):
        """Метод для чтения и возврата данных json-файла"""
        if os.path.exists(file_path):
            with open(_file_worker, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return data
        else:
            return []

    def add_to_json_file(self, file_path, new_data):
        """Метод для добавления новых данных в json-файл"""
        data = self.read_json_file(file_path)
        data.extend(new_data)

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def delete_vacancy(self, _file_worker, vacancy_name):
        with open(_file_worker, 'r', encoding='utf-8') as file:
            data = json.load(file)

        data = [data for vacancy in data if vacancy['name'] == vacancy_name]

        with open(_file_worker, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
