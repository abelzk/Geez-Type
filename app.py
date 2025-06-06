# import threading
# from geez_engine import start_typing, stop_typing, toggle_typing
# import pystray
# from pystray import MenuItem as item
# from PIL import Image, ImageDraw
# import keyboard

# typing_thread = threading.Thread(target=start_typing, daemon=True)
# def create_image():
#     image = Image.new('RGB', (64, 64), 'white')
#     draw = ImageDraw.Draw(image)
#     draw.text((10, 20), "አ", fill="black")
#     return image

# def on_toggle(icon, item):
#     toggle_typing()

# def on_quit(icon, item):
#     stop_typing()
#     icon.stop()

# def main():
#     keyboard.add_hotkey('ctrl+shift+space', toggle_typing)
#     typing_thread.start()

#     icon = pystray.Icon("amharic_typing")
#     icon.icon = create_image()
#     icon.menu = pystray.Menu(
#         item('Toggle Amharic Typing (Ctrl+Shift+space)', on_toggle),
#         item('Quit', on_quit)
#     )
#     icon.run()
# አቤል ዘካርsስkfፍ ክፍሉ ገብረ Yይ
# አበlለል ዘከካረር
# ዘዘዘzዘዘዘዘዘዘዘzዘዘዘዘዘዘዘዘzዘዘዘዘዘዘzዘዘ
# አቤል ዘካርsስአበቤለልዘከካረርየያሰስ
#xቤ

# if __name__ == '__main__':
#     main()
# main.py
import keyboard
import threading
from pynput.keyboard import Controller

from geez_engine import syllable_engine, toggle_typing, start_typing

if __name__ == "__main__":

    print("Amharic Typing Software Started")
    print("Press Ctrl + Space to toggle Amharic typing on/off")

    # Toggle typing mode with Ctrl + Space
    keyboard.add_hotkey('ctrl+space', toggle_typing)

    # Start the typing hook in a separate thread
    threading.Thread(target=start_typing, daemon=True).start()

    # Keep the program running
    keyboard.wait()
