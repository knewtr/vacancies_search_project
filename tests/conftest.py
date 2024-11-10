import pytest


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
    return {"name": "test1", "url": "test1", "salary": 1, "requirements": "test1", "responsibility": "test1"}

@pytest.fixture
def vacancy_2():
    return {"name": "test2", "url": "test2", "salary": 2, "requirements": "test2", "responsibility": "test2"}

@pytest.fixture
def no_salary_vacancy():
    return