import subprocess
import threading
import time
import keyboard

# --- CONFIGURATION ---
WINDOW_COUNT = 50  # Number of CMD windows to open
OPEN_DELAY = 0.1  # Delay in seconds between opening windows to prevent system overload
HOTKEY_TO_CLOSE = "space"  # Keyboard key to trigger closing all windows
# ---------------------

close_all = False


def open_cmd_windows(count=WINDOW_COUNT):
    for i in range(count):
        if close_all:
            break
        subprocess.Popen("start cmd", shell=True)
        time.sleep(OPEN_DELAY)
    print(f"✅ Opened {count} CMD windows")


def close_cmd_windows():
    global close_all
    close_all = True
    subprocess.run("taskkill /f /im cmd.exe", shell=True)
    print("🧹 All CMD windows closed!")


def wait_for_hotkey():
    print(f"⌨️ Press {HOTKEY_TO_CLOSE.upper()} to close all windows...")
    keyboard.wait(HOTKEY_TO_CLOSE)
    close_cmd_windows()


if __name__ == "__main__":
    print("🚀 Starting program...")

    hotkey_thread = threading.Thread(target=wait_for_hotkey, daemon=True)
    hotkey_thread.start()

    open_cmd_windows()

    if not close_all:
        print(f"🟢 All windows opened. Press {HOTKEY_TO_CLOSE.upper()} to close.")
        hotkey_thread.join()
