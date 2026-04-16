import tkinter as tk
from tkinter import simpledialog
import pygetwindow as gw
import pyautogui
from PIL import Image, ImageTk

selected_window = None

def select_window():
    global selected_window

    windows = gw.getAllTitles()
    windows = [w for w in windows if w.strip() != ""]

    win_name = simpledialog.askstring(
        "Select Window",
        "Enter window name (example: Chrome, Notepad):\n\n" + "\n".join(windows[:20])
    )

    if win_name:
        try:
            selected_window = gw.getWindowsWithTitle(win_name)[0]
            status_label.config(text=f"Selected: {win_name}")
        except:
            status_label.config(text="❌ Window not found!")

def rotate_180():
    if not selected_window:
        status_label.config(text="❌ No window selected!")
        return

    try:
        x, y = selected_window.topleft
        w, h = selected_window.size

        # Take screenshot of the window
        screenshot = pyautogui.screenshot(region=(x, y, w, h))

        # Rotate 180 degrees
        rotated = screenshot.rotate(180)

        # Show result
        show_image(rotated)

    except Exception as e:
        status_label.config(text=f"Error: {e}")

def show_image(img):
    top = tk.Toplevel(root)
    top.title("Rotated 180°")

    tk_img = ImageTk.PhotoImage(img)
    label = tk.Label(top, image=tk_img)
    label.image = tk_img
    label.pack()

# GUI
root = tk.Tk()
root.title("180° Window Rotator")
root.geometry("300x200")

btn_select = tk.Button(root, text="Select Window", command=select_window)
btn_select.pack(pady=15)

btn_rotate = tk.Button(root, text="Rotate 180°", command=rotate_180)
btn_rotate.pack(pady=15)

status_label = tk.Label(root, text="No window selected")
status_label.pack(pady=10)

root.mainloop()