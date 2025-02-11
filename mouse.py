from pynput import mouse, keyboard
from recog import recog

class Main:
    def __init__(self):
        self.mouseListener = None
        self.holdingCtrl = False
        self.mouse_coords = []
        with keyboard.Listener(
                on_press=self.kbd_press,
                on_release=self.kbd_release) as listener:
            self.listener = listener
            listener.join()
    
    def mouse_move(self, x, y):
        self.mouse_coords.append((x, -y))
    
    def kbd_press(self, key):
        if self.listener.canonical(key) == keyboard.Key.ctrl:
            self.mouse_coords = []
            self.mouseListener = mouse.Listener(
                on_move=self.mouse_move
            )
            self.mouseListener.start()
            self.holdingCtrl = True
        
        if key == keyboard.Key.f12 and self.holdingCtrl:
            print('YAY!')

    def kbd_release(self, key):
        key = self.listener.canonical(key)
        if key == keyboard.Key.ctrl:
            self.holdingCtrl = False
            recog(self.mouse_coords.copy())
            self.mouseListener.stop()

Main()
