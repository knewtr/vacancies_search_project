from abc import ABC, abstractmethod
import requests

class Parser(ABC):
    """Абстрактный родительский класс для подключения к API"""
    def __init__(self):
        pass

    @abstractmethod
    def get_response(self, keyword, per_page):
        """Абстрактный метод для получения ответа от API"""
        pass

    @abstractmethod
    def get_vacancies(self, keyword, per_page):
        """Абстрактный метод для получения данных в формате json"""
        pass
