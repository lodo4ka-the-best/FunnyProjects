import subprocess
import threading
import time
import sys

try:
    import keyboard
except ImportError:
    print("❌ Install 'keyboard': pip install keyboard")
    sys.exit(1)


WINDOW_COUNT = 50
OPEN_DELAY = 0.1
HOTKEY_TO_CLOSE = "space"

stop_event = threading.Event()
procs = []
procs_lock = threading.Lock()


def open_cmd_windows(count: int) -> int:
    opened = 0
    for i in range(count):
        if stop_event.is_set():
            break
        try:
            p = subprocess.Popen("cmd", creationflags=subprocess.CREATE_NEW_CONSOLE)
            with procs_lock:
                procs.append(p)
            opened += 1
        except OSError as e:
            print(f"⚠️  Failed to open window #{i + 1}: {e}")
        time.sleep(OPEN_DELAY)

    print(f"✅ Opened {opened} of {count} windows")
    return opened


def close_cmd_windows() -> None:
    if stop_event.is_set():
        return
    stop_event.set()

    with procs_lock:
        snapshot = list(procs)

    for p in snapshot:
        if p.poll() is None:
            try:
                p.terminate()
            except Exception as e:
                print(f"⚠️  terminate() error: {e}")

    deadline = time.time() + 2.0
    for p in snapshot:
        remaining = deadline - time.time()
        if remaining <= 0:
            break
        try:
            p.wait(timeout=remaining)
        except subprocess.TimeoutExpired:
            try:
                p.kill()
            except Exception:
                pass

    closed = sum(1 for p in snapshot if p.poll() is not None)
    print(f"🧹 Closed {closed} windows")


def wait_for_hotkey() -> None:
    print(f"⌨️  Press {HOTKEY_TO_CLOSE.upper()} to close all windows...")
    try:
        keyboard.wait(HOTKEY_TO_CLOSE)
    except Exception as e:
        print(f"⚠️  Hotkey wait error: {e}")
        return
    close_cmd_windows()


def main() -> None:
    print("🚀 Starting program...")

    hotkey_thread = threading.Thread(target=wait_for_hotkey, name="hotkey-listener", daemon=True)
    hotkey_thread.start()

    try:
        open_cmd_windows(WINDOW_COUNT)
        if not stop_event.is_set():
            print(f"🟢 All windows opened. Press {HOTKEY_TO_CLOSE.upper()} to close them.")
            while hotkey_thread.is_alive():
                hotkey_thread.join(timeout=0.5)
    except KeyboardInterrupt:
        print("\n⚠️  Interrupted by user (Ctrl+C).")
        close_cmd_windows()
    finally:
        if not stop_event.is_set():
            close_cmd_windows()
        try:
            keyboard.unhook_all()
        except Exception:
            pass
        print("👋 Program finished.")


if __name__ == "__main__":
    main()
