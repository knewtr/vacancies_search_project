from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy


def get_vacancy_list(vacancies_list_dict: list[dict]) -> list[Vacancy]:
    """Функция возвращает список экземпляров класса Vacancy из списка словарей"""
    vacancy_list = list(map(lambda x: Vacancy.new_vacancy(HeadHunterAPI.get_vacancy_list(x)), vacancies_list_dict))
    return vacancy_list


def filter_vacancies(vacancies: list[Vacancy], filter_words: list[str]) -> list[Vacancy]:
    """Функция фильтрации вакансий по ключевым словам"""
    filtered_vacancies = []
    for vacancy in vacancies:
        for word in filter_words:
            if word.lower() in vacancy.description.lower():
                filtered_vacancies.append(vacancy)
                continue
    return filtered_vacancies


def get_vacancies_by_salary(filtered_vacancies: list[Vacancy], salary_range: str) -> list[Vacancy]:
    """Функция фильтрации вакансий по заработной плате"""
    ranged_vacancies = []
    vac_range = list(map(lambda x: int(x), salary_range.split(" - ")))
    range_min = vac_range[0]
    range_max = vac_range[-1]
    for vacancy in filtered_vacancies:
        if (vacancy.salary >= range_min) and (vacancy.salary <= range_max):
            ranged_vacancies.append(vacancy)
    return ranged_vacancies


def sort_vacancies(ranged_vacancies: list[Vacancy]) -> list[Vacancy]:
    """Функция сортировки вакансий по заработной плате"""
    sorted_vacancies = sorted(ranged_vacancies, key=lambda v: v.salary, reverse=True)
    return sorted_vacancies


def get_top_vacancies(sorted_vacancies: list[Vacancy], top_n: int) -> list[Vacancy]:
    """Функция выводит топ-N вакансий по заработной плате"""
    top_vacancies = []
    for i in range(top_n):
        if i < len(sorted_vacancies):
            vacancy = sorted_vacancies[i]
            top_vacancies.append(vacancy)
    return top_vacancies


def print_vacancies(top_vacancies):
    """Функция выводит список топ-N вакансий"""
    for vacancy in top_vacancies:
        print(vacancy)


# if __name__ == "__main__":
#     vac1 = Vacancy.new_vacancy({'name': 'test1', 'url': 'test1', 'salary': 10000, 'description': 'test1'})
#     vac2 = Vacancy.new_vacancy({'name': 'test2', 'url': 'test2', 'salary': 20000, 'description': 'test2'})
#     vac3 = Vacancy.new_vacancy({'name': 'test3', 'url': 'test3', 'salary': 30000, 'description': 'test3'})
#     vac4 = Vacancy.new_vacancy({'name': 'test4', 'url': 'test4', 'salary': 40000, 'description': 'test4'})
#     vac5 = Vacancy.new_vacancy({'name': 'test5', 'url': 'test5', 'salary': 50000, 'description': 'test5'})
#     v_list = [vac1, vac2, vac3, vac4, vac5]
#
#     filtered_words = ['test']
#     filtered_list = filter_vacancies(v_list, filtered_words)
#     print(filtered_list)
#
#     salary_range = '15000 - 40000'
#     ranged_list = get_vacancies_by_salary(filtered_list, salary_range)
#
#     sorted_list = sort_vacancies(ranged_list)
#
#     top_list = get_top_vacancies(sorted_list, 4)
#     print_vacancies(top_list)
