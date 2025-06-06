import threading
from geez_engine import start_typing, stop_typing, toggle_typing
import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
import keyboard

typing_thread = threading.Thread(target=start_typing, daemon=True)
def create_image():
    image = Image.new('RGB', (64, 64), 'white')
    draw = ImageDraw.Draw(image)
    draw.text((10, 20), "አ", fill="black")
    return image

def on_toggle(icon, item):
    toggle_typing()

def on_quit(icon, item):
    stop_typing()
    icon.stop()

def main():
    keyboard.add_hotkey('ctrl+shift+space', toggle_typing)
    typing_thread.start()

    icon = pystray.Icon("amharic_typing")
    icon.icon = create_image()
    icon.menu = pystray.Menu(
        item('Toggle Amharic Typing (Ctrl+Shift+space)', on_toggle),
        item('Quit', on_quit)
    )
    icon.run()
if __name__ == '__main__':
    main()
