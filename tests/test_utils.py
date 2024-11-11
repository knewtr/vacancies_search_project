from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies

def test_filter_vacancies(vac1, vac2):
    vac_list = [vac1, vac2]
    filtered_list = filter_vacancies(vac_list, ['test1'])
    assert filtered_list[0] == vac1

def test_get_vacancies_by_salary(vac1, vac2):
    salary_range = '10000 - 12000'
    vacancies = [vac1, vac2]
    result = get_vacancies_by_salary(vacancies, salary_range)
    assert result == [vac1]

# def test_sort_vacancies(vac_list):
#     res = sort_vacancies(vac_list)
#     assert res.get('salary') == [20000, 10000] #см. комментарий в utils
