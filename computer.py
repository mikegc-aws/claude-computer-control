import pyautogui
from PIL import Image
import io
import base64
import time
import pynput
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController

class Computer:
    def __init__(self):
        self.display_width_px, self.display_height_px = pyautogui.size()
        pyautogui.FAILSAFE = False
        self.mouse = MouseController()
        self.keyboard = KeyboardController()

    def key(self, keys):

        # Convert keys to lowercase
        keys = keys.lower()

        print(f"Pressing keys: {keys}")

        keys = keys.split('+')

        print(f"Split keys: {keys}")

        special_keys = {
            'return': Key.enter,
            'page_down': Key.page_down,
            'page_up': Key.page_up,
            'ctrl': Key.cmd,
            'control_l': Key.ctrl_l,
            'control_r': Key.ctrl_r,
            'alt': Key.alt,
            'shift': Key.shift,
            'escape': Key.esc,
            'space': Key.space,
            'backspace': Key.backspace,
            'tab': Key.tab,
            'end': Key.end,
            'capslock': Key.caps_lock,
            'left_arrow': Key.left,
            'right_arrow': Key.right,
            'up_arrow': Key.up,
            'down_arrow': Key.down,
            'up': Key.up,
            'left': Key.left,
            'right': Key.right,
            'down': Key.down,
            'f1': Key.f1,
            'f2': Key.f2,
            'f3': Key.f3,
            'f4': Key.f4,
            'f5': Key.f5,
            'f6': Key.f6,
            'f7': Key.f7,
            'f8': Key.f8,
            'f9': Key.f9,
            'f10': Key.f10,
            'f11': Key.f11,
            'f12': Key.f12,
            'xf86audioraisevolume': Key.media_volume_up,
            'xf86audiolowervolume': Key.media_volume_down,
            'xf86audiovolumemute': Key.media_volume_mute,
        }

        processed_keys = []
        for k in keys:
            processed_keys.append(special_keys.get(k, k))

        # Press all keys in the processed_keys list
        for key in processed_keys:
            print(f"Pressing key: {key}")
            if isinstance(key, str):
                self.keyboard.press(key)
            elif isinstance(key, Key):
                self.keyboard.press(key)
            time.sleep(0.05)  # Reduced delay between key presses

        # Release all keys in reverse order
        for key in reversed(processed_keys):
            print(f"Releasing key: {key}")
            if isinstance(key, str):
                self.keyboard.release(key)
            elif isinstance(key, Key):
                self.keyboard.release(key)
            time.sleep(0.05)  # Reduced delay between key releases

        time.sleep(0.1)

    def type(self, text):
        pyautogui.write(text)
        time.sleep(0.1)

    def left_click_drag(self, x, y):
        pyautogui.mouseDown()
        pyautogui.dragTo(x, y, duration=0.5)
        pyautogui.mouseUp()
        time.sleep(0.1)

    def mouse_move(self, x, y):
        pyautogui.moveTo(x, y)
        time.sleep(0.1)

    def left_click(self):
        pyautogui.click()
        time.sleep(0.1)

    def right_click(self):
        pyautogui.rightClick()
        time.sleep(0.1)

    def middle_click(self):
        pyautogui.middleClick()
        time.sleep(0.1)

    def double_click(self):
        self.mouse.click(Button.left, 2)
        time.sleep(0.1)

    def screenshot(self):
        screenshot = pyautogui.screenshot()
        buffered = io.BytesIO()
        screenshot.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()

    def cursor_position(self):
        x, y = pyautogui.position()
        return x, y


if __name__ == "__main__":
    time
    computer = Computer()
    computer.key("ctrl+a")
