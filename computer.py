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

    def key(self, key):
        if key == 'Return':
            self.keyboard.press(Key.enter)
            time.sleep(0.1)
            self.keyboard.release(Key.enter)
        else:
            self.keyboard.press(key)
            time.sleep(0.1)
            self.keyboard.release(key)
        time.sleep(0.1)

    def type(self, text):
        pyautogui.write(text)
        time.sleep(0.1)

    def mouse_move(self, x, y):
        pyautogui.moveTo(x, y)
        time.sleep(0.1)

    def left_click(self):
        pyautogui.click()
        time.sleep(0.1)

    def left_click_drag(self, start_x, start_y, end_x, end_y, duration=0.5):
        pyautogui.mouseDown(start_x, start_y)
        pyautogui.moveTo(end_x, end_y, duration=duration)
        pyautogui.mouseUp()
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
        return {"x": x, "y": y}

