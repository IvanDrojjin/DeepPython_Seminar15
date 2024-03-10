'''
Задание №2
На семинаре про декораторы был создан логирующий
декоратор. Он сохранял аргументы функции и результат её
работы в файл.
Напишите аналогичный декоратор, но внутри используйте
модуль logging

deco_class_8.py
'''

import logging

LOG_FILE = 'deco_class_8_ex.log'


class LogEx:
    """Класс-декоратор"""

    def __init__(self):
        # Настройка конфигурации логгера
        logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def __call__(self, func):
        def decorated(*args, **kwargs):
            """Обертка"""
            res = func(*args, **kwargs)
            log_str = f'log: {func.__name__}({args}, {kwargs}) = {res}'
            # print(log_str)
            # Запись информации в лог-файл
            logging.info(log_str)
            return res

        return decorated


@LogEx()
def my_func(val_1, val_2):
    """Вычисление"""
    return val_1 ** val_2


def f0():
    print('-- Функции с декораторами --')
    # my_func = Log()(my_func)
    my_func(1, 5)  # my_func = LogEx()(my_func)
    my_func(2, 5)
    my_func(3, 5)
    my_func(4, 5)



    # другой подход применения декоратора к функции func2 = LogEx()(func2)
    # func2 = LogEx()(func2)
    # func2(4, 5)


if __name__ == "__main__":
    f0()
