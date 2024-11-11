from src.vacancy import Vacancy


def test_print_vacancy(capsys):
    vacancy_1 = Vacancy(name="name_test1", url="url_test1", salary=10000, responsibility="resp_test1", requirements="req_test1")
    print(vacancy_1)
    message = capsys.readouterr()
    expected_output = f"Вакансия: name_test1\nСсылка: url_test1\nЗарплата: 10000\n" f"Обязанности: resp_test1\nТребования: req_test1\n"
    assert message.out == expected_output


def test_compare_salary(vacancy_1, vacancy_2):
    assert (vacancy_1["salary"] < vacancy_2["salary"]) is True
    assert (vacancy_1["salary"] > vacancy_2["salary"]) is False
    assert (vacancy_1["salary"] <= vacancy_2["salary"]) is True
    assert (vacancy_1["salary"] >= vacancy_2["salary"]) is False


def test_new_vacancy(vacancy_1, test_vacancy_1):
    test_vacancy_1 = Vacancy.new_vacancy(vacancy_1)
    assert test_vacancy_1.name == "name_test1"
    assert test_vacancy_1.url == "url_test1"
    assert test_vacancy_1.salary == 10000
    assert test_vacancy_1.requirements == "req_test1"
    assert test_vacancy_1.responsibility == "resp_test1"
