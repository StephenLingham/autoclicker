# Script to automate running in Valheim

import keyboard
import time

running = False
sprinting = False
timeWhenSprintStarted = time.time()
timeWhenRestStarted = time.time()

while True:
  time.sleep(0.1)
  if not running and keyboard.is_pressed('+'):
    running = True
    keyboard.press("w")

  if running and keyboard.is_pressed('-'):
    running = False
    keyboard.release("w")

  if running:
    if sprinting:
      timeSpentSprinting = time.time() - timeWhenSprintStarted
      if timeSpentSprinting > 6:
        sprinting = False
        timeWhenRestStarted = time.time()
        keyboard.release("left shift")
    if not sprinting:
      timeSpentResting = time.time() - timeWhenRestStarted
      if timeSpentResting > 2:
        sprinting = True
        timeWhenSprintStarted = time.time()
        keyboard.press("left shift")

  if keyboard.is_pressed('*'):
    break
