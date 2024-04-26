import pyautogui
import time
pyautogui.FAILSAFE = False
times = 0
while True:
  # Get the current mouse position
  current_position = pyautogui.position()

  # Move the mouse to the lower left corner and click
  print('Moving mouse to the lower left corner')
  pyautogui.moveTo(0, pyautogui.size().height)
  print('Clicking')
  pyautogui.click()

  # Move the mouse back to the original position
  print('Moving mouse back to the original position')
  pyautogui.moveTo(*current_position)

  # Wait for a minute
  print('Last moved time: ', time.strftime('%H:%M:%S'))
  times += 1
  print('Times moved: ', times)
  time.sleep(60)

