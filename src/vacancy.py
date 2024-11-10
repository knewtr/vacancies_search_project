from src.base_vacancy import BaseVacancy


class Vacancy(BaseVacancy):
    """Класс для работы с данными вакансий"""

    __slots__ = ("name", "url", "salary", "responsibility", "requirements")

    def __init__(self, name, url, salary, responsibility, requirements):
        self.name = name
        self.url = url
        self.salary = salary
        self.requirements = requirements
        self.responsibility = responsibility

    def __str__(self):
        return (
            f"Вакансия: {self.name}\nСсылка: {self.url}\nЗарплата: {self.salary}\n"
            f"Обязанности: {self.responsibility}\nТребования: {self.requirements}"
        )

    @property
    def vacancy_dict(self):
        """Метод возвращает словарь вакансии"""
        return {
            "name": self.name,
            "url": self.url,
            "salary": self.salary,
            "responsibility": self.responsibility,
            "requirements": self.requirements,
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
    def __is_salary(salary: int | str | None) -> int:
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
        objects_list = []
        for vacancy in vacancies:
            objects_list.append(
                cls(
                    vacancy.get("name"),
                    vacancy.get("url"),
                    vacancy.get("salary"),
                    vacancy.get("responsibility"),
                    vacancy.get("requirements"),
                )
            )
        return objects_list

    @classmethod
    def new_vacancy(cls, new_vacancy_dict: dict):
        """Метод позволяет инициализировать новую вакансию"""
        name = new_vacancy_dict.get("name")
        url = new_vacancy_dict.get("url")
        salary = Vacancy.__is_salary(new_vacancy_dict.get("salary"))
        responsibility = new_vacancy_dict.get("responsibility")
        requirements = new_vacancy_dict.get("requirements")
        return cls(name, url, salary, responsibility, requirements)
