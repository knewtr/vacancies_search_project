from src.hh_api import HeadHunterAPI
from src.vacancy import Vacancy
from src.utils import filter_vacancies, get_vacancies_by_salary, sort_vacancies, get_top_vacancies, print_vacancies, \
    get_vacancy_list


def user_interaction():
    """Основная функция проекта для взаимодействия с пользователем"""
    # platforms = ["HeadHunter"]
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    hh_api = HeadHunterAPI()

    hh_vacancies = hh_api.get_vacancies(search_query)

    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)

if __name__ == "__main__":
    user_interaction()