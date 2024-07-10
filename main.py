import csv
import pyautogui
import time
import keyboard

print("Press F1 to start pasting commands, and press ESC to exit.")
commands_csv = []

with open('commands.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        commands_csv.append(row[0])

typing_speed = 0.09  # seconds per character

typing_in_progress = False

def type_commands():
    global typing_in_progress
    typing_in_progress = True
    for command in commands_csv:
        pyautogui.write(command, interval=typing_speed)
        pyautogui.press('enter')
        time.sleep(0.9)  # Wait between sending commands
    typing_in_progress = False

def on_press_F1(event):
    print("F1 pressed. Starting typing...")
    type_commands()

keyboard.on_press_key("f1", on_press_F1)
keyboard.wait('esc')
