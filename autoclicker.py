# Script to automate clicking in clicker games

import pyautogui as gui
import keyboard

gui.PAUSE = 0.01

clicking = False

while True:
  if not clicking and keyboard.is_pressed('+'):
    clicking = True

  if clicking and keyboard.is_pressed('-'):
    clicking = False

  if clicking:
    gui.click()

  if keyboard.is_pressed('*'):
    break
