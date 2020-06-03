import threading

from encryption import encryption


class MyThread(threading.Thread):

    def __init__(self, input_text, key):
        super().__init__()
        self.output_text = None
        self.input_text = input_text
        self.key = key

    def run(self):
        self.output_text = encryption(self.input_text, self.key)
