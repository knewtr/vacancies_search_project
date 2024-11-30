import pytest

from src.vacancy import Vacancy


@pytest.fixture
def test_vacancy_1():
    return {
        "name": "Python Developer/Разработчик Python",
        "salary": {
            "from": 10000,
            "to": None,
        },
        "alternate_url": "https://hh.ru/vacancy/108374935",
        "snippet": {
            "requirement": "опыт работы с Docker.",
            "responsibility": "Поддержание системы. - Разработка нового функционала.",
        },
    }


@pytest.fixture
def test_vacancy_2():
    return {
        "name": "Python Developer/Разработчик Python",
        "salary": {
            "from": 15000,
            "to": 30000,
        },
        "alternate_url": "https://hh.ru/vacancy/108374935",
        "snippet": {
            "requirement": "опыт работы с Docker.",
            "responsibility": "Поддержание системы. - Разработка нового функционала.",
        },
    }


@pytest.fixture
def test_vacancy_3():
    return {
        "name": "Python Developer/Разработчик Python",
        "salary": {
            "from": None,
            "to": None,
        },
        "alternate_url": "https://hh.ru/vacancy/108374935",
        "snippet": {
            "requirement": "опыт работы с Docker.",
            "responsibility": "Поддержание системы. - Разработка нового функционала.",
        },
    }


@pytest.fixture
def vacancy_1():
    return {
        "name": "name_test1",
        "url": "url_test1",
        "salary": 10000,
        "responsibility": "resp_test1",
        "requirements": "req_test1",
    }


@pytest.fixture
def vacancy_2():
    return {
        "name": "name_test2",
        "url": "url_test2",
        "salary": 20000,
        "responsibility": "resp_test2",
        "requirements": "req_test2",
    }


@pytest.fixture
def vac1():
    return Vacancy("name_test1", "url_test1", 10000, "resp_test1", "req_test1")


@pytest.fixture
def vac2():
    return Vacancy("name_test2", "url_test2", 20000, "resp_test2", "req_test2")


@pytest.fixture
def vac_list():
    vac1 = Vacancy("name_test1", "url_test1", 10000, "resp_test1", "req_test1")
    vac2 = Vacancy("name_test2", "url_test2", 20000, "resp_test2", "req_test2")
    vac3 = Vacancy("name_test3", "url_test3", 30000, "resp_test3", "req_test3")
    vac4 = Vacancy("name_test4", "url_test4", 40000, "resp_test4", "req_test4")
    listed_vacancies = [vac1, vac2, vac3, vac4]
    return listed_vacancies


@pytest.fixture
def expected_list():
    return [
        "Вакансия: name_test4\nСсылка: url_test4\nЗарплата: 40000\nОбязанности: resp_test4\nТребования: req_test4",
        "Вакансия: name_test3\nСсылка: url_test3\nЗарплата: 30000\nОбязанности: resp_test3\nТребования: req_test3",
        "Вакансия: name_test2\nСсылка: url_test2\nЗарплата: 20000\nОбязанности: resp_test2\nТребования: req_test2",
        "Вакансия: name_test1\nСсылка: url_test1\nЗарплата: 10000\nОбязанности: resp_test1\nТребования: req_test1",
    ]


@pytest.fixture
def vacancy2():
    return Vacancy("name_test2", "url_test2", 20000, "resp_test2", "req_test2")


@pytest.fixture
def vacancy3():
    return Vacancy("name_test3", "url_test3", 30000, "resp_test3", "req_test3")


@pytest.fixture
def vacancy4():
    return Vacancy("name_test4", "url_test4", 40000, "resp_test4", "req_test4")


@pytest.fixture
def sorted_list(vacancy4, vacancy3, vacancy2):
    sorted_l = [vacancy4, vacancy3, vacancy2]
    return sorted_l


@pytest.fixture
def vacancies1():
    vacancies1 = [
        {
            "name": "name_test1",
            "url": "url_test1",
            "salary": 10000,
            "responsibility": "resp_test1",
            "requirements": "req_test1",
        },
        {
            "name": "name_test2",
            "url": "url_test2",
            "salary": 20000,
            "responsibility": "resp_test2",
            "requirements": "req_test2",
        },
    ]
    return vacancies1
