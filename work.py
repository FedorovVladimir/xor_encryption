from MyThread import MyThread

COUNT_CHARS_FOR_READ = 1024 * 1024


def work(input_file_path: str, output_file_path: str, key: str):
    with open(input_file_path, 'rb') as input_file, open(output_file_path, 'wb') as output_file:
        threads = []

        input_text = input_file.read(COUNT_CHARS_FOR_READ)
        while input_text != b'':
            thread = MyThread(input_text, key)
            threads.append(thread)
            thread.start()
            input_text = input_file.read(COUNT_CHARS_FOR_READ)

        for thread in threads:
            thread.join()
            output_file.write(thread.output_text)
