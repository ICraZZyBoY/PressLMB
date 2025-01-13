import tkinter as tk
import pyautogui
import time

click = 0

def button_click():
    global click
    if (click == 0):
        time.sleep(5)
        pyautogui.mouseDown()
        button.config(text = "Стоп")
    else:
        pyautogui.mouseUp()
        button.config(text = "Зажать ЛКМ")
    click = ((click + 1) % 2)

# Создаем главное окно
window = tk.Tk()
window.title("Простое приложение")

# Создаем кнопку
button = tk.Button(window, text="Зажать ЛКМ", command=button_click)
button.pack(pady=20)  # pady - вертикальный отступ

# Запускаем главный цикл обработки событий
window.mainloop()
