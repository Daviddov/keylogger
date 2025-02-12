from pynput import keyboard

def key_pressed(key):
    print(key.char)
def listen():
    listiner = keyboard.Listener(on_press=key_pressed)
    listiner.start()
    input()
    listiner.stop()

listen()