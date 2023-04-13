from src.utils import sort_data, filter_data, format_data


def test_sort_data(test_data):
    sorted_data = sort_data(test_data)
    assert [x['date'] for x in sorted_data] == ['2019-08-26T10:50:58.294041',
                                                '2019-07-03T18:35:29.512364',
                                                '2018-12-24T20:16:18.819037',
                                                '2018-06-30T02:08:58.425572',
                                                '2018-03-23T10:45:06.972075']


def test_filter_data(test_data):
    filted_data = filter_data(test_data)
    assert [x['state'] for x in filted_data] == ['EXECUTED',
                                                 'EXECUTED', 'EXECUTED',
                                                 'EXECUTED']


def test_format_data(test_data):
    formatt_data = format_data(test_data)
    assert [formatted_data for formatted_data in formatt_data] == ['\n'
                                                                   '26.08.2019 Перевод организации\n'
                                                                   'Maestro 1596 83** **** 5199 ->  Счет 6468 64** '
                                                                   '**** 9589\n'
                                                                   '31957.58 руб.\n'
                                                                   '        ',
                                                                   '\n'
                                                                   '03.07.2019 Перевод организации\n'
                                                                   'MasterCard 7158 30** **** 6758 ->  Счет 3538 30** '
                                                                   '**** 5560\n'
                                                                   '8221.37 USD\n'
                                                                   '        ',
                                                                   '\n'
                                                                   '30.06.2018 Перевод организации\n'
                                                                   'Счет 7510 68** **** 6952 ->  Счет 1177 66** **** '
                                                                   '6702\n'
                                                                   '9824.07 USD\n'
                                                                   '        ',
                                                                   '\n'
                                                                   '24.12.2018 Перевод со счета на счет\n'
                                                                   'Счет 7168 74** **** 5290 ->  Счет 8744 85** **** '
                                                                   '9781\n'
                                                                   '991.49 руб.\n'
                                                                   '        ',
                                                                   '\n'
                                                                   '23.03.2018 Открытие вклада\n'
                                                                   'Новый счет    Счет 4142 15** **** 2431\n'
                                                                   '48223.05 руб.\n'
                                                                   '        ']