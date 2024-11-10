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
            "to": 80000,
        },
        "alternate_url": "https://hh.ru/vacancy/108374935",
        "snippet": {
            "requirement": "опыт работы с Docker.",
            "responsibility": "Поддержание системы. - Разработка нового функционала.",
        },
    }
