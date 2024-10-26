# Program that captures keystrokes during game sessions
import keyboard
from datetime import datetime

# Generate timestamp and filename for session
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
file_name = f'keystroke_log_{timestamp}'

# Event handler for capturing keystrokes
def get_key(event):
    print(event.name)
    save_to_file(event.name)

# Write keystrokes to .txt file
def save_to_file(key):
    with open(file_name, 'a') as log:
        log.write(key+ '\n')

# Start keyboard event listener
keyboard.on_press(get_key)

# Stop logging session
keyboard.wait('esc')

# Stop capturing keystrokes
keyboard.unhook_all()