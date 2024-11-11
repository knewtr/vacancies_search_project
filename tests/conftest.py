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
    return {'name':'name_test1', 'url':'url_test1', 'salary':10000, 'responsibility' : 'resp_test1', 'requirements':'req_test1'}


@pytest.fixture
def vacancy_2():
    return {'name':'name_test2', 'url':'url_test2', 'salary':20000, 'responsibility' : 'resp_test2', 'requirements':'req_test2'}


@pytest.fixture
def vac1():
    return Vacancy('name_test1', 'url_test1', 10000, 'resp_test1', 'req_test1')

@pytest.fixture
def vac2():
    return Vacancy('name_test2', 'url_test2', 20000, 'resp_test2', 'req_test2')

@pytest.fixture
def vac_list():
    listed_vacancies = [Vacancy('name_test1', 'url_test1', 10000, 'resp_test1', 'req_test1'),
                        Vacancy('name_test2', 'url_test2', 20000, 'resp_test2', 'req_test2')]
    return listed_vacancies