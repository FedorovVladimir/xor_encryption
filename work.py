from encryption import encryption

COUNT_CHARS_FOR_READ = 1024 * 1024


def work(input_file_path: str, output_file_path: str, key: str):
    with open(input_file_path, 'rb') as input_file, open(output_file_path, 'wb') as output_file:
        input_text = input_file.read(COUNT_CHARS_FOR_READ)
        output_text = encryption(input_text, key)
        output_file.write(output_text)
