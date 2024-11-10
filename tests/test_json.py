import json

from src.json_manager import JSONSaver


def test_not_found_file_print(capsys):
    obj = JSONSaver(file_worker='data/test.json')
    captured = capsys.readouterr()
    assert captured.out == "Файл не существует\n"

# def test_add_vacancy():
#     result = JSONSaver(file_worker='vacancies.json')
#     with open('data/test_vacancy.json', 'w', encoding='utf-8') as file:
#         data = json.load(file)
#         assert result is None
