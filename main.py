import click


@click.command()
@click.option("-i", "input_file", required=True, help="Путь до файла для обработки")
@click.option("-o", "output_file", required=True, help="Путь до выходного файла")
@click.option("-k", "key", required=True, help="Ключ шифрования")
def process(input_file: str, output_file: str, key: str):
    pass


if __name__ == "__main__":
    process()
