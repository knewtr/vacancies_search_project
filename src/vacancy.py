from src.base_vacancy import BaseVacancy


class Vacancy(BaseVacancy):
    """Класс для работы с данными вакансий"""

    __slots__ = ("name", "url", "_salary", "requirements", "responsibility")

    def __init__(self, name, url, _salary, requirements, responsibility):
        self.name = name
        self.url = url
        self._salary = _salary
        self.requirements = requirements
        self.responsibility = responsibility

    def __str__(self):
        return (
            f"Вакансия: {self.name}\n, Ссылка: {self.url}\n, Зарплата: {self._salary}\n"
            f"Требования: {self.requirements}\n, Обязанности: {self.responsibility}\n"
        )

    def __le__(self, other):
        """Метод сравнения по зарплате <="""
        return self._salary <= other.salary

    def __lt__(self, other):
        """Метод сравнения по зарплате <"""
        return self._salary < other.salary

    def __ge__(self, other):
        """Метод сравнения по зарплате >="""
        return self._salary >= other.salary

    def __gt__(self, other):
        """Метод сравнения по зарплате >"""
        return self._salary > other.salary


    @staticmethod
    def salary(salary: int | None | str) -> int:
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
    def new_vacancy(cls, new_vacancy_dict):
        """Метод позволяет инициализировать новую вакансию"""
        name = new_vacancy_dict.get('name')
        url = new_vacancy_dict.get('url')
        salary = Vacancy.salary(new_vacancy_dict.get('salary'))
        requirements = new_vacancy_dict.get('requirements')
        responsibility = new_vacancy_dict.get('responsibility')

    @property
    def vacancy_dict(self):
        """Метод возвращает словарь вакансии"""
        return {
            'name': self.name,
            'url': self.url,
            'salary': self.salary,
            'requirements': self.requirements,
            'responsibility': self.responsibility,
        }
