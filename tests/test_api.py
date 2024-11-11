from src.hh_api import HeadHunterAPI


def test_headhunter_api():
    test = HeadHunterAPI()
    assert test.url == "https://api.hh.ru/vacancies"
    assert test.headers == {"User-Agent": "HH-User-Agent"}
    assert test.params == {"text": "", "page": 0, "per_page": 100, "only_with_salary": True}


# def test_get_vacancy_list(test_vacancy_1, test_vacancy_2, test_vacancy_3):
#     assert HeadHunterAPI.get_vacancy_formatted(test_vacancy_1) == {
#         "name": "Python Developer/Разработчик Python",
#         "url": "https://hh.ru/vacancy/108374935",
#         "salary": 10000,
#         "description": "Обязанности: Поддержание системы. - Разработка нового функционала. Требования: опыт работы с Docker.",
#     }
#
#     assert HeadHunterAPI.get_vacancy_formatted(test_vacancy_2) == {
#         "name": "Python Developer/Разработчик Python",
#         "url": "https://hh.ru/vacancy/108374935",
#         "salary": 22500,
#         "description": "Обязанности: Поддержание системы. - Разработка нового функционала. Требования: опыт работы с Docker.",
#         }
#
#     assert HeadHunterAPI.get_vacancy_formatted(test_vacancy_3) == {
#         "name": "Python Developer/Разработчик Python",
#         "url": "https://hh.ru/vacancy/108374935",
#         "salary": 80000,
#         "description": "Обязанности: Поддержание системы. - Разработка нового функционала. Требования: опыт работы с Docker.",
#         }
