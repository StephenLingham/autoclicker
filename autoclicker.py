import pyautogui as gui
import keyboard

gui.PAUSE = 0.01

clicking = False

while True:
  if not clicking and keyboard.is_pressed('+'):
    clicking = True
    print("Started clicking")

  if clicking and keyboard.is_pressed('-'):
    clicking = False
    print("Stopped clicking")

  if clicking:
    gui.click()

  if keyboard.is_pressed('*'):
    break
