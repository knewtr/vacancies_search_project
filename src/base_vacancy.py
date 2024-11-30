from abc import ABC, abstractmethod


class BaseVacancy(ABC):
    """Абстрактный родительский класс для работы с данными вакансии"""

    @classmethod
    @abstractmethod
    def new_vacancy(cls, *arg, **kwargs):
        """Метод позволяет инициализировать новую вакансию"""
        pass

    @abstractmethod
    def __le__(self, other):
        """Метод сравнения по зарплате <="""
        pass

    @abstractmethod
    def __lt__(self, other):
        """Метод сравнения по зарплате <"""
        pass

    @abstractmethod
    def __ge__(self, other):
        """Метод сравнения по зарплате >="""
        pass

    @abstractmethod
    def __gt__(self, other):
        """Метод сравнения по зарплате >"""
        pass
