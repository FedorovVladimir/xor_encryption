import shutil
import click

from work import work


@click.command()
@click.option("-i", "input_file_path", required=True, help="Путь до файла для обработки")
@click.option("-o", "output_file_path", required=True, help="Путь до выходного файла")
@click.option("-k", "key", required=True, help="Ключ шифрования")
def process(input_file_path: str, output_file_path: str, key: str):
    # проверка входного файла на существование
    try:
        input_file = open(input_file_path)
        input_file.close()
    except FileNotFoundError:
        print("Входной файл не найден")
        exit(1)

    # проверка выходного файла на существование
    try:
        output_file = open(output_file_path)
        output_file.close()
        end = False
        while not end:
            answer = input("Выходной файл уже существует. Перезаписать? [y/n]").lower()
            if answer == 'n' or answer == 'т':
                exit(1)
            elif answer == 'y' or answer == 'н':
                end = True
    except FileNotFoundError:
        pass

    work(input_file_path, key)
    shutil.move("~temp", output_file_path)


if __name__ == "__main__":
    process()
