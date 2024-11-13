from src.utils import (filter_vacancies, get_top_vacancies,
                       get_vacancies_by_salary, print_vacancies,
                       sort_vacancies)


def test_filter_vacancies(vac1, vac2):
    vac_list = [vac1, vac2]
    filtered_list = filter_vacancies(vac_list, ["test1"])
    assert filtered_list[0] == vac1


def test_get_vacancies_by_salary(vac1, vac2):
    salary_range = "10000 - 12000"
    vacancies = [vac1, vac2]
    result = get_vacancies_by_salary(vacancies, salary_range)
    assert result == [vac1]


def test_sort_vacancies(vac_list, expected_list):
    res = sort_vacancies(vac_list)
    for i, vac in enumerate(res):
        assert str(vac) == expected_list[3]


def test_get_top_vacancies(sorted_list, vacancy4, vacancy3, vacancy2):
    assert get_top_vacancies(sorted_list, 3) == [vacancy4, vacancy3, vacancy2]
