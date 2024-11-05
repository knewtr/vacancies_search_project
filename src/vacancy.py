class Vacancy:
    """Класс для работы с данными вакансий"""
    __slots__ = ('name', 'url', '_salary', 'requirements', 'responsibility')
    def __init__(self, name, url, _salary, requirements, responsibility):
        self.name = name
        self.url = url
        self._salary = _salary
        self.requirements = requirements
        self.responsibility = responsibility

    def __ge__(self, other):
        """Метод сравнения вакансий по начальной заработной плате"""
        return self._salary >= other.salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        """Метод валидации данных о зарплате"""
        if value < 0:
            raise ValueError('Зарплата не указана')
        self._salary = value
