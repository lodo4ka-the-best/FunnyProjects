# 🎉 Funny Projects

A collection of small, silly, and sometimes mildly chaotic Python scripts.
No serious purpose. No grand mission. Just code that does something funny — and hopefully doesn't break your computer in the process.

> ⚠️ **Disclaimer:** These projects are for fun and educational purposes only. Use them responsibly. Don't run anything on a machine you don't own or without permission.

---

## 📦 Projects

### 💻 CMD Spammer

Opens a configurable number of `cmd.exe` windows on Windows, then waits for a single key press to close them all gracefully.

Perfect for:
- Pranking a friend who left their laptop unlocked 🫣
- Testing how many console windows your system can handle 😅
- Learning about `subprocess`, threads, and global hotkeys in Python

#### ✨ Features
- 🪟 Opens any number of CMD windows you want (default: **50**)
- ⏱️ Configurable delay between openings to avoid overloading the system
- ⌨️ One hotkey (**SPACE** by default) closes everything
- 🧹 Only closes the windows **it opened itself** — never touches other `cmd.exe` processes
- 🛡️ Graceful shutdown: `terminate()` → wait → `kill()` fallback
- 🧵 Thread-safe, race-condition-free, and `Ctrl+C` friendly

#### 📋 Requirements
- **Windows** (uses `CREATE_NEW_CONSOLE` and `cmd.exe`)
- **Python 3.8+**
- The `keyboard` module:
  ```bash
  pip install keyboard
  ```

#### ⚙️ Configuration
Edit the top of `cmd_spammer.py`:

```python
WINDOW_COUNT      = 50      # How many CMD windows to open
OPEN_DELAY        = 0.1     # Delay between openings (seconds)
HOTKEY_TO_CLOSE   = "space" # Key to close all windows
```

#### 🚀 Usage
```bash
python cmd_spammer.py
```

Then:
1. Watch the chaos unfold as dozens of CMD windows pop up 🪟🪟🪟
2. Press **SPACE** when you've had enough
3. All windows close cleanly ✅


#### ⚠️ Notes
- On some systems, the `keyboard` module requires **administrator privileges** for global hotkey capture. If the hotkey doesn't respond, run your terminal as administrator.
- If your PC is weak, increase `OPEN_DELAY` (e.g., to `0.3`) to give it some breathing room.
- 50 windows is a lot. 200 is a lot more. You have been warned. 😄

#### 🧠 What you can learn from this
- Launching processes with `subprocess.Popen` and `creationflags`
- Clean process termination (`terminate` vs `kill`)
- Thread synchronization with `threading.Event` and `threading.Lock`
- Handling global hotkeys safely

---

## 🤝 Contributing

Got a funny idea? Open a PR. Bonus points if it makes someone laugh *and* still runs without crashing.

## 📜 License

Do whatever you want. Just don't blame us if your friend gets mildly annoyed. 😄
