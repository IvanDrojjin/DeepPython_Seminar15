import os
import logging
from collections import namedtuple

LOG_FILE = 'hw15_tsk6.log'
# Настройка конфигурации логгера
logging.basicConfig(filename=LOG_FILE, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Создание объекта namedtuple для хранения информации о содержимом файла или каталога
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])


def get_file_info(file_path):
    file_info_list = []

    for item in os.listdir(file_path):
        full_path = os.path.join(file_path, item)

        name, extension = os.path.splitext(item)
        is_directory = os.path.isdir(full_path)
        parent_directory = os.path.basename(os.path.dirname(full_path))

        file_info = FileInfo(
            name=name if is_directory else name + extension,
            extension=extension if not is_directory else '',
            is_directory=is_directory,
            parent_directory=parent_directory
        )

        file_info_list.append(file_info)

        # Запись информации в лог-файл
        logging.info(
            f"Name: {file_info.name}, Extension: {file_info.extension}, Is Directory: {file_info.is_directory}, Parent Directory: {file_info.parent_directory}")

    return file_info_list


if __name__ == "__main__":
    import sys

    # 'hw15_tsk6.py'

    if len(sys.argv) != 2:
        # print("Usage: python program_name.py path_to_directory")
        print(f"Usage: python {sys.argv[0]} path_to_directory")
    else:
        directory_path = sys.argv[1]
        file_info_list = get_file_info(directory_path)
