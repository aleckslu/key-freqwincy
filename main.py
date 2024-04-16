import json
from pynput.keyboard import Key, Listener
import ctypes
import psutil

JSON_FILE_NAME = "key-freq.json"
BACKUP_FILE_NAME = "key-freq-backup.json"
SAVE_INTERVAL = 50

KEY_FREQ_DATA = {}
total_keypresses = 0

def load_and_backup_file():
    global KEY_FREQ_DATA

    try:
        with open(JSON_FILE_NAME, "r") as f:
            KEY_FREQ_DATA = json.load(f)

            with open(BACKUP_FILE_NAME, "w") as b:
                json.dump(KEY_FREQ_DATA, b, indent=2)

    except Exception as e:
        print("Error loading or backingup data: ", e)


def get_active_window_process_name():
    """Gets the process ID for a given Win32Window object."""
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    # hwnd = win32gui.GetForegroundWindow()  # Get the handle of the active window
    user32 = ctypes.WinDLL('user32')
    hwnd = user32.GetForegroundWindow()
    process_id = ctypes.c_ulong()
    print(process_id)
    user32.GetWindowThreadProcessId(hwnd, ctypes.byref(process_id))
    # pid = process_id.value
    # print(pid)

    try:
        process = psutil.Process(process_id.value)
        return process.name() 

    except (psutil.NoSuchProcess, psutil.AccessDenied, KeyboardInterrupt) as e:
        return "Unknown-Process"

def on_press(key):
    global KEY_FREQ_DATA, total_keypresses

    process_name = get_active_window_process_name()

    # Create nested objects if they don't exist
    KEY_FREQ_DATA.setdefault(process_name, {})
    KEY_FREQ_DATA[process_name].setdefault(str(key), 0)

    # Increment key press count
    KEY_FREQ_DATA[process_name][str(key)] += 1
    total_keypresses += 1

    # print(f"{total_keypresses}. {process_name}:  {key} - {KEY_FREQ_DATA[process_name][str(key)]}")
    # Save data to JSON every 1000 keypresses
    if total_keypresses % 50 == 0:
        save_data_to_json()

def save_data_to_json():
    global KEY_FREQ_DATA

    with open(JSON_FILE_NAME, "w") as f:
        json.dump(KEY_FREQ_DATA, f, indent=2)

    print("data saved")
    print(KEY_FREQ_DATA)
    # Reset count and data (optional: keep history by not resetting)
    # key_presses = {}

def on_release(key):
    if str(key) == "\\x03":
        # Stop listener
        return False

load_and_backup_file()

# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    try:
        listener.join()
    except (KeyboardInterrupt, Exception) as e:
        # Allow the user to exit the program with Ctrl+C
        if e:
            print(e)
        else:
            print("Keyboard interrupt received. Exiting...")