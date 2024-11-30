from src.hh_api import HeadHunterAPI


def test_headhunter_api():
    test = HeadHunterAPI()
    assert test.url == "https://api.hh.ru/vacancies"
    assert test.headers == {"User-Agent": "HH-User-Agent"}
    assert test.params == {"text": "", "page": 0, "per_page": 100, "only_with_salary": True}
