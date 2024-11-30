import requests

from src.parser import Parser


class HeadHunterAPI(Parser):
    """Класс для работы с API HeadHunter"""

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100, "only_with_salary": True}
        self._vacancies = []
        super().__init__()

    @property
    def url(self):
        return self.__url

    @property
    def headers(self):
        return self.__headers

    @property
    def params(self):
        return self.__params

    def _Parser__get_response(self):
        """Метод подключения к API"""
        response = requests.get("https://api.hh.ru/", headers=self.__headers, params=self.__params)
        status_code = response.status_code
        self.__params["page"] = 0
        if status_code == 200:
            print("Ответ от hh.ru получен.")
            return True
        else:
            print(f"Ошибка подключения к hh.ru.")
            return False

    def get_vacancies(self, keyword, per_page=10):
        """Метод для получения данных в формате json"""
        vacancies = []
        if self._Parser__get_response():
            self.__params["text"] = keyword
            self.__params["per_page"] = per_page
            while requests.get(self.__url, headers=self.__headers, params=self.__params):
                response = requests.get(self.__url, headers=self.__headers, params=self.__params)
                vacancies.extend(response.json()["items"])
                self.__params["page"] += 1
        return vacancies


# if __name__ == "__main__":
#     HeadHunterAPI().get_vacancies("Python")
