import keyboard
import time

jumping = False
timeWhenJumped = time.time()

while True:
  time.sleep(0.1)
  if not jumping and keyboard.is_pressed('+'):
    jumping = True

  if jumping and keyboard.is_pressed('-'):
    jumping = False

  if jumping:    
    timeSinceLastJumped = time.time() - timeWhenJumped
    if (timeSinceLastJumped > 1.5):
      timeWhenJumped = time.time()
      keyboard.press_and_release("space")

  if keyboard.is_pressed('*'):
    break
