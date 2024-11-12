from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy

# def get_vacancy_list(vacancies_list_dict):
#     """Функция возвращает список экземпляров класса Vacancy из списка словарей"""
#     formatted_vacancies = map(lambda x: HeadHunterAPI.get_vacancy_formatted(x), vacancies_list_dict)
#     vacancy_list = [Vacancy.new_vacancy(vacancy) for vacancy in formatted_vacancies]
#     return vacancy_list


def filter_vacancies(vacancies: list, filter_words: list[str]) -> list:
    """Функция фильтрации вакансий по ключевым словам"""
    filtered_vacancies = []
    for vacancy in vacancies:
        print(vacancy)
        for word in filter_words:
            if vacancy.requirements.lower() is None:
                print(vacancy)
            if word.lower() in vacancy.requirements.lower() or word.lower() in vacancy.responsibility.lower():
                filtered_vacancies.append(vacancy)
                continue
    return filtered_vacancies


def get_vacancies_by_salary(vacancies: list, salary_range: str) -> list:
    """Функция фильтрации вакансий по заработной плате"""
    ranged_vacancies = []
    vac_range = list(map(lambda x: int(x.strip()), salary_range.split(" - ")))
    range_min = vac_range[0]
    range_max = vac_range[-1]
    for vacancy in vacancies:
        if range_min <= vacancy.salary <= range_max:
            ranged_vacancies.append(vacancy)
    return ranged_vacancies


def sort_vacancies(ranged_vacancies):
    """Функция сортировки вакансий по заработной плате"""
    sorted_vacancies = sorted(ranged_vacancies, key=lambda v: v.salary, reverse=True)
    return sorted_vacancies


def get_top_vacancies(sorted_vacancies, top_n):
    """Функция выводит топ-N вакансий по заработной плате"""
    top_vacancies = []
    for i in range(top_n):
        if i < len(sorted_vacancies):
            vac = sorted_vacancies[i]
            top_vacancies.append(vac)
    return top_vacancies


def print_vacancies(top_vacancies):
    """Функция выводит список топ-N вакансий"""
    for v in top_vacancies:
        print(v)


# if __name__ == "__main__":
#     # vac1 = Vacancy.new_vacancy({'name':'name_test1', 'url':'url_test1', 'salary':10000, 'responsibility' : 'resp_test1', 'requirements':'req_test1'})
#     # vac2 = Vacancy.new_vacancy({'name':'name_test2', 'url':'url_test2', 'salary':20000, 'responsibility' : 'resp_test2', 'requirements':'req_test2'})
#     # vac3 = Vacancy.new_vacancy({'name':'name_test3', 'url':'url_test3', 'salary':50000, 'responsibility' : 'resp_test3', 'requirements':'req_test3'})
#
#     # v_list = [vac1, vac2, vac3]
#
#     # filtered_list = filter_vacancies(v_list, ['test'])
#
#     # salary_ranged = '15000 - 40000'
#     # ranged_list = get_vacancies_by_salary(filtered_list, salary_ranged)
#     # for vac in filtered_list:
#     #     print(vac) # Чтобы получить 1 вакансию, нужно преобразовать vac1,2,3 так, чтобы был объект Vacancy
#
#     vac1 = Vacancy('name_test1', 'url_test1', 10000, 'resp_test1', 'req_test1')
#     vac2 = Vacancy('name_test2', 'url_test2', 20000, 'resp_test2', 'req_test2')
#     vac3 = Vacancy('name_test3', 'url_test3', 30000, 'resp_test3', 'req_test3')
#     vac4 = Vacancy('name_test4', 'url_test4', 40000, 'resp_test4', 'req_test4')
#     ranged_list = [vac1, vac2, vac3, vac4]
#     sorted_list = sort_vacancies(ranged_list)
#
#     top_list = get_top_vacancies(sorted_list, 3)
#     print_vacancies(top_list)
