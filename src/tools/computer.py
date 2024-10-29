import pyautogui
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
from typing import Tuple
import base64
from io import BytesIO
import time

class Computer:
    """
    A class to interact with the computer's input devices and screen.
    """

    def __init__(self):
        self.display_width_px, self.display_height_px = pyautogui.size()
        pyautogui.FAILSAFE = False
        self.mouse = MouseController()
        self.keyboard = KeyboardController()

    def get_screen_size(self) -> Tuple[int, int]:
        """
        Get the screen size in pixels.

        Returns:
            Tuple[int, int]: The width and height of the screen in pixels.
        """
        return self.display_width_px, self.display_height_px

    def move_mouse(self, x: int, y: int) -> None:
        """
        Move the mouse to the specified coordinates.

        Args:
            x (int): The x-coordinate to move to.
            y (int): The y-coordinate to move to.
        """
        pyautogui.moveTo(x, y)
        time.sleep(0.1)

    def click_mouse(self, button: str = 'left') -> None:
        """
        Perform a mouse click.

        Args:
            button (str): The mouse button to click ('left', 'right', or 'middle').
        """
        if button == 'left':
            pyautogui.click()
        elif button == 'right':
            pyautogui.rightClick()
        elif button == 'middle':
            pyautogui.middleClick()
        time.sleep(0.1)

    def type_text(self, text: str) -> None:
        """
        Type the specified text.

        Args:
            text (str): The text to type.
        """
        pyautogui.write(text)
        time.sleep(0.1)

    def press_key(self, keys: str) -> None:
        """
        Press keyboard key(s).

        Args:
            keys (str): The key(s) to press, separated by '+' for combinations.
        """
        keys = keys.lower().split('+')
        special_keys = {
            'return': Key.enter,
            'page_down': Key.page_down,
            'page_up': Key.page_up,
            'ctrl': Key.cmd,
            'super': Key.cmd,
            'command': Key.cmd,
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

        processed_keys = [special_keys.get(k, k) for k in keys]

        for key in processed_keys:
            if isinstance(key, str):
                self.keyboard.press(key)
            elif isinstance(key, Key):
                self.keyboard.press(key)
            time.sleep(0.05)

        for key in reversed(processed_keys):
            if isinstance(key, str):
                self.keyboard.release(key)
            elif isinstance(key, Key):
                self.keyboard.release(key)
            time.sleep(0.05)

        time.sleep(0.1)

    def double_click(self) -> None:
        self.mouse.click(Button.left, 2)
        time.sleep(0.1)

    def take_screenshot(self) -> str:
        """
        Take a screenshot and return it as a base64 encoded string.

        Returns:
            str: The base64 encoded screenshot image.
        """
        screenshot = pyautogui.screenshot()
        buffered = BytesIO()
        screenshot.save(buffered, format="PNG")
        return base64.b64encode(buffered.getvalue()).decode()

    def left_click_drag(self, x: int, y: int) -> None:
        """
        Perform a left-click drag operation to the specified coordinates.

        Args:
            x (int): The x-coordinate to drag to.
            y (int): The y-coordinate to drag to.
        """
        pyautogui.mouseDown()
        pyautogui.dragTo(x, y, duration=0.5)
        pyautogui.mouseUp()
        time.sleep(0.1)

    def get_cursor_position(self) -> Tuple[int, int]:
        """
        Get the current cursor position.

        Returns:
            Tuple[int, int]: The x and y coordinates of the cursor.
        """
        x, y = pyautogui.position()
        return x, y
