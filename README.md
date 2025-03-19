Automated Keyboard Presser GUI

This simple Python project allows users to automate keyboard inputs through an easy-to-use graphical user interface (GUI). It continuously presses a specified key at customizable intervals and durations, making it ideal for games or tasks that require repetitive keystrokes.

---

🚀 Features
- Easy-to-use GUI built with Tkinter.
- Customizable settings: Specify the key to press, duration of key press, and interval between presses.
- Hotkey controls: Quickly start (F8) and stop (F9) the automation.
- Compatibility: Uses `pydirectinput` for improved game compatibility.

---

📦 Installation

Requirements
- Python 3.6+

Install dependencies:
```bash
pip install tkinter pydirectinput keyboard pyinstaller
```

Running the Application

To launch the GUI directly:
```bash
python auto_key_gui.py
```

Create Windows Executable
To convert the application into a standalone Windows executable:

```bash
pyinstaller --onefile --noconsole auto_key_gui.py
```

Then find the executable in the `dist/` directory.

---

🖥 Usage

1. Launch the GUI.
2. Enter the desired key, press duration, and interval.
3. Click **Start** or press **F8** to begin automation.
4. Click **Stop** or press **F9** to end automation.

---

⚠️ Important Notes
- Administrator privileges might be necessary for certain games to detect the automated inputs.
- Use responsibly; ensure automated key pressing complies with your game's or application's terms of service.

---

🔧 Technologies
- Python 3
- Tkinter
- Pydirectinput
- Keyboard
- PyInstaller


---

📬 Contact
For any questions or suggestions, feel free to open an issue or contact me directly!

