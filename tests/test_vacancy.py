from src.vacancy import Vacancy


def test_print_vacancy(capsys):
    vacancy_1 = Vacancy(name="test1", url="test1", salary=1, responsibility="test1", requirements="test1")
    print(vacancy_1)
    message = capsys.readouterr()
    expected_output = f"Вакансия: test1\nСсылка: test1\nЗарплата: 1\n" f"Обязанности: test1\nТребования: test1\n"
    assert message.out == expected_output


def test_compare_salary(vacancy_1, vacancy_2):
    assert (vacancy_1["salary"] < vacancy_2["salary"]) is True
    assert (vacancy_1["salary"] > vacancy_2["salary"]) is False
    assert (vacancy_1["salary"] <= vacancy_2["salary"]) is True
    assert (vacancy_1["salary"] >= vacancy_2["salary"]) is False


def test_new_vacancy(vacancy_1):
    test_vacancy_1 = Vacancy.new_vacancy(vacancy_1)
    assert test_vacancy_1.name == "test1"
    assert test_vacancy_1.url == "test1"
    assert test_vacancy_1.salary == 1
    assert test_vacancy_1.requirements == "test1"
    assert test_vacancy_1.responsibility == "test1"
