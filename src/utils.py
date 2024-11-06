

def filter_vacancies(vacancies_list, filter_words):
    """Метод фильтрации вакансий по ключевым словам"""
    filtered_vacancies = []
    for vacancy in vacancies_list:
        if filter_words in vacancy:
            filtered_vacancies.append(vacancy)
        return filtered_vacancies

def get_vacancies_by_salary(filtered_vacancies, salary_range):
    """Метод фильтрации вакансий по заработной плате"""
    ranged_vacancies = []
    for vacancy in filtered_vacancies:
        if salary_range in vacancy['salary']:
            ranged_vacancies.append(vacancy)
        return ranged_vacancies

def sort_vacancies(ranged_vacancies):
    """Метод сортировки вакансий по заработной плате"""
    sorted_vacancies = sorted(ranged_vacancies.items(), key=lambda item: item[1])
    return sorted_vacancies

def get_top_vacancies(sorted_vacancies, top_n):
    """Метод выводит топ-N вакансий по заработной плате"""
    top_vacancies = []
    for i in range(top_n):
        vacancy = sorted_vacancies[i]
        top_vacancies.append(vacancy)
        return top_vacancies

def print_vacancies(top_vacancies):
    """Метод выводит список топ-N вакансий"""
    return top_vacancies