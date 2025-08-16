# Python Keylogger (Educational Project)

## Project Description
This is a simple keylogger built in Python using the `pynput` library.  
The program records keystrokes in real-time and saves them into a text file (`keylog.txt`).  
It was developed purely for **educational and research purposes** to understand how system input listeners work.  

**Disclaimer**: This project is not intended for malicious use. Please run it only on your own device for learning/testing.  

---

## Features
- Captures and logs keystrokes in real-time.  
- Handles special keys such as:
  - `Space` → recorded as a space.  
  - `Enter` → creates a new line.  
  - `Backspace` → recorded as `[BACKSPACE]`.  
- Ignores unnecessary modifier keys (like `Shift`).  
- Stops logging when the **Escape (ESC)** key is pressed.  

---

## How It Works
1. Runs a keyboard listener in the background.  
2. Each key press is sent to `write_to_file()`.  
3. Logs are appended into `keylog.txt`.  
4. Pressing `ESC` safely exits the program.  
