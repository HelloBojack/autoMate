from pynput import mouse
from PyQt6.QtCore import pyqtSignal, QThread

class GlobalKeyboardListen(QThread):
    mouse_middle_signal = pyqtSignal()
    def __init__(self):
        super().__init__()

    def run(self):
        def on_click(x, y, button, pressed):
            if button == mouse.Button.middle:
                if pressed:
                    self.mouse_middle_signal.emit()
                    print("鼠标中键按下")
                    return True
        # 创建鼠标监听器

        with mouse.Listener(on_click=on_click) as mouse_listener:
            mouse_listener.join()