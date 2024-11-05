from abc import ABC

from src.parser import Parser
import requests


class HeadHunterAPI(Parser):
    """Класс для работы с API HeadHunter"""

    def __init__(self):
        self._url = 'https://api.hh.ru/vacancies'
        self._headers = {'User-Agent': 'HH-User-Agent'}
        self._params = {'text': '', 'page': 0, 'per_page': 100}
        self._vacancies = []
        super().__init__()

    def _get_response(self, keyword, per_page):
        """Метод подключения к API"""
        self._params["text"] = keyword
        self._params["per_page"] = per_page
        return requests.get(self._url, params=self._params)

    def get_vacancies(self, keyword, per_page):
        """Метод для получения данных в формате json"""
        vacancy_response = self._get_response(keyword, per_page).json()["items"]
        return vacancy_response

    # def load_vacancies(self, keyword):
    #     self.params['text'] = keyword
    #     while self.params.get('page') != 20:
    #         response = requests.get(self.url, headers=self.headers, params=self.params)
    #         vacancies = response.json()['items']
    #         self.vacancies.extend(vacancies)
    #         self.params['page'] += 1
