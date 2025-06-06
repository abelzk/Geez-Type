# amharic_typing.py
import json
import os
import keyboard
from pynput.keyboard import Controller, Key

kb = Controller()
buffer = ""
active = True  # Typing toggle flag
CONFIG_FILE = "geez_map.json"

vowel_order = {
    "A": 0, "u": 1, "i": 2, "a": 3,
    "y": 4, "e": 5, "o": 6
}
if len(buffer) == 2:
    buffer = ""

def load_syllable_map(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Syllable map file not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

syllable_map = load_syllable_map(CONFIG_FILE)

def is_modifier(key):
    return key in {
        'shift', 'ctrl', 'alt', 'alt gr', 'windows', 'caps lock',
        'space', 'enter', 'backspace', 'tab', 'esc', 'delete',
        'home', 'end', 'page up', 'page down', 'insert', 'up',
        'down', 'left', 'right', 'f1', 'f2', 'f3', 'f4', 'f5',
        'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'print screen',
        'scroll lock', 'pause', 'num lock', 'numpad 0', 'numpad 1',
        'numpad 2', 'numpad 3', 'numpad 4', 'numpad 5', 'numpad 6',
        'numpad 7', 'numpad 8', 'numpad 9'
    }

def press_backspace(times=1):
    for _ in range(times):
        kb.press(Key.backspace)
        kb.release(Key.backspace)
def type_text(text):
    for char in text:
        kb.press(char)
        kb.release(char)

def syllable_engine(event):
    global buffer, active, last_time

    if not active or event.event_type != "down":
        return
    

    key = event.name
    if len(key) > 1 or key in ['shift', 'alt', 'windows', 'ctrl']:
        return
    
    # Ignore modifiers and multi-character keys
    if is_modifier(key) or keyboard.is_pressed('ctrl') or keyboard.is_pressed('alt') or keyboard.is_pressed('windows'):
        return
    if len(key) != 1:
        return

    # if key in ['space' 'enter']:
    #     buffer = ""
    
    try:
        # if key in vowel_order and buffer:
        if len(buffer) == 1 and buffer in syllable_map and key in vowel_order:
            consonant = buffer
            buffer = ""
            if consonant in syllable_map:
                # Nyala
                # .hook(syllable_engine, suppress=True)
                syllable = syllable_map[consonant][vowel_order[key]]
                type_text('\b' * 2 + syllable)  # Backspace twice to remove consonant and space
                return
            elif key in syllable_map:
                buffer = key
                # # keyboard.hook(syllable_engine, suppress=False)
                # type_text('\b' + syllable_map[key][0])
                keyboard.send('backspace')
                keyboard.write(syllable_map[key][0])
                return
            elif key in vowel_order:
                # buffer = key
                # keyboard.hook(syllable_engine, suppress=True)
                keyboard.send('backspace')
                return
            if key == 'space' or key in ['enter', 'tab', 'backspace', 'tab', '.', ',', '?', '!', ';', ':', '-', '_', '=', '+', '*', '/', '\\', '|', '(', ')', '[', ']', '{', '}', '"', "'", '`']:
                buffer = ""
            
            else:
                buffer += key
                if len(buffer) >= 2:
                    # If buffer exceeds 2 characters, reset it
                    buffer = ""
                if len(buffer) == 1 and buffer in syllable_map and key in vowel_order:
                    # If buffer has only one character, type it directly
                    type_text(buffer)
                    buffer = ""

        # Single consonant
        if key in syllable_map:
            buffer = key
            press_backspace()
            type_text(syllable_map[key][0])
            return
        elif key in vowel_order:
            press_backspace()
            return
        else:
            buffer = ""
    except Exception as e:
        print(f"Error processing key '{key}': {e}")
        buffer = ""

def start_typing():
    keyboard.hook(syllable_engine, suppress=True)

def stop_typing():
    keyboard.unhook_all()

def toggle_typing():
    global active
    active = not active
    print(f"Amharic Typing {'Enabled' if active else 'Disabled'}")
