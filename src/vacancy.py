from src.base_vacancy import BaseVacancy


class Vacancy(BaseVacancy):
    """Класс для работы с данными вакансий"""

    __slots__ = ("name", "url", "salary", "description")

    def __init__(self, name, url, salary, description):
        self.name = name
        self.url = url
        self.salary = salary
        self.description = description

    def __str__(self):
        return (
            f"Вакансия: {self.name}\n, Ссылка: {self.url}\n, Зарплата: {self.salary}\n"
            f"Описание: {self.description}\n"
        )

    @property
    def vacancy_dict(self):
        """Метод возвращает словарь вакансии"""
        return {
            "name": self.name,
            "url": self.url,
            "salary": self.salary,
            "description": self.description,
        }

    def __le__(self, other):
        """Метод сравнения по зарплате <="""
        return self.salary <= other.salary

    def __lt__(self, other):
        """Метод сравнения по зарплате <"""
        return self.salary < other.salary

    def __ge__(self, other):
        """Метод сравнения по зарплате >="""
        return self.salary >= other.salary

    def __gt__(self, other):
        """Метод сравнения по зарплате >"""
        return self.salary > other.salary

    @staticmethod
    def _is_salary(salary: int | str | None) -> int:
        """Метод валидации данных о зарплате"""
        if salary is None or (type(salary) is str and not salary.isdigit()):
            return 0
        elif type(salary) is str and salary.isdigit():
            return int(salary)
        else:
            return salary

    @classmethod
    def cast_to_object_list(cls, vacancies: list[dict]):
        """Метод возвращает список объектов класса Vacancy из списка словарей"""
        return [cls(**vacancy) for vacancy in vacancies]

    @classmethod
    def new_vacancy(cls, new_vacancy_dict: dict):
        """Метод позволяет инициализировать новую вакансию"""
        name = new_vacancy_dict.get("name")
        url = new_vacancy_dict.get("url")
        salary = Vacancy._is_salary(new_vacancy_dict.get("salary", 0))
        description = new_vacancy_dict.get("description")
        return cls(name, url, salary, description)
