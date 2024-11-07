from src.vacancy import Vacancy


def filter_vacancies(vacancies_list: list[Vacancy], filter_words: list[str]) -> list[Vacancy]:
    """Функция фильтрации вакансий по ключевым словам"""
    filtered_vacancies = []
    for vacancy in vacancies_list:
        for word in filter_words:
            if word.lower() in vacancy.requirements.lower() or vacancy.responsibility.lower():
                filtered_vacancies.append(vacancy)
                continue
    return filtered_vacancies


def get_vacancies_by_salary(filtered_vacancies: list[Vacancy], salary_range: str) -> list[Vacancy]:
    """Функция фильтрации вакансий по заработной плате"""
    ranged_vacancies = []
    vac_range = list(map(lambda x: int(x), salary_range.split(' - ')))
    range_min = vac_range[0]
    range_max = vac_range[-1]
    for vacancy in filtered_vacancies:
        if (vacancy.salary >= range_min) and (vacancy.salary <= range_max):
            ranged_vacancies.append(vacancy)
        return ranged_vacancies


def sort_vacancies(ranged_vacancies: list[Vacancy]) -> list[Vacancy]:
    """Функция сортировки вакансий по заработной плате"""
    sorted_vacancies = sorted(ranged_vacancies, key=lambda x: x.salary, reverse=True)
    return sorted_vacancies


def get_top_vacancies(sorted_vacancies: list[Vacancy], top_n: int) -> list[Vacancy]:
    """Функция выводит топ-N вакансий по заработной плате"""
    top_vacancies = []
    for i in range(top_n):
        vacancy = sorted_vacancies[i]
        top_vacancies.append(vacancy)
        return top_vacancies


def print_vacancies(top_vacancies):
    """Функция выводит список топ-N вакансий"""
    for vacancy in top_vacancies:
        print(vacancy)

if __name__ == "__main__":
    vac1 = Vacancy.new_vacancy({"id": 123, "name": "name", "description": "test", "url": "test", "salary": 7})
    vac2 = Vacancy.new_vacancy({"id": 124, "name": "name", "description": "test", "url": "test", "salary": 2})
    vac3 = Vacancy.new_vacancy({"id": 125, "name": "name", "description": "test", "url": "test", "salary": 5})
    vac4 = Vacancy.new_vacancy({"id": 126, "name": "name", "description": "test", "url": "test", "salary": 10})
    vac5 = Vacancy.new_vacancy({"id": 127, "name": "name", "description": "test", "url": "test", "salary": 1})
    vac6 = Vacancy.new_vacancy({"id": 128, "name": "name", "description": "test", "url": "test", "salary": 3})
    v_list = [vac1, vac2, vac3, vac4, vac5, vac6]
    sort_list = sort_vacancies(v_list)
    top_n_list = get_top_vacancies(sort_list, 4)
    print_vacancies(top_n_list)