import tkinter as tk
from tkinter import ttk
from gpiozero import LED
import datasource


class LEDButton(ttk.Button):
    def __init__(self, master, led, **kwargs):
        super().__init__(master, **kwargs)
        self.led = led
        self.state= False
        self.configure(command=self.user_click)
        s = ttk.style()
        s.theme_use('clam')
        s.configure(Title, Tlabel, font=('Arial', 20))
        s.configure('LEDClose, TButton', font=('Arial', 20), borderwidth=5, padding=(10, 20))
        s.configure('LEDOpen, TButton', background='yellow', font=('Arial', 20), borderwidth=5, padding=(10, 20))

    def user_click(self):
        self.state = not self.state
        if self.state:
            self.configure(text='LED 關')
            self.configure(style='LEDOpen.TButton')
            self.led.on()
            datasource.insert_data(1)
        else:
            self.configure(text='LED 開')
            self.configure(style='LEDClose.TButton') 
            self.led.off()
            datasource.insert_data(0)
            
class Window(tk.Tk):
    def __init__(self, redLed, **kwargs):
        
        super().__init__(**kwargs)
        
        self.title("這是我的第一個視窗")
        self.resizable(False, False)
        s = ttk.Style()
        s.theme_use('clam')
        s.configure('Title.TLabel', font=('Arial, 20'))
        
        title_label = ttk.Label(self, text="LED控制器", style=('Title.TLabel')
        title_label.pack(pady=25, padx=100)

        self.led_btn = LEDButton(self, led=redLed text="LED 開", style='LEDClose.TButton')
        self.led_btn.pack(pady=(10, 50))


if __name__ == "__main__":


    led = LED(23)
    led.off()
    window = Window(led)
    window.mainloop()
