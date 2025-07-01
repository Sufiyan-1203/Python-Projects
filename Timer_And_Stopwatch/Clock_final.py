import tkinter as tk
from tkinter import messagebox
import time

def open_stopwatch():
    sw = tk.Toplevel(root)
    sw.title("Stopwatch")
    sw.geometry("300x200")
    sw.config(bg="#1e1e1e")
    
    sw_display = tk.Label(sw, text="00:00:00", font=("Courier", 30), fg="lime", bg="black", width=10, bd=3, relief="sunken")
    sw_display.pack(pady=20)
    
    sw_running = [False]
    sw_start_time = [0]
    sw_elapsed = [0]

    def format_sw(t):
        m = int(t // 60)
        s = int(t % 60)
        ms = int((t - int(t)) * 100)
        return f"{m:02}:{s:02}:{ms:02}"

    def update_sw():
        if sw_running[0]:
            now = time.time()
            elapsed = now - sw_start_time[0] + sw_elapsed[0]
            sw_display.config(text=format_sw(elapsed))
            sw.after(10, update_sw)

    def start_sw():
        if not sw_running[0]:
            sw_start_time[0] = time.time()
            sw_running[0] = True
            update_sw()

    def stop_sw():
        if sw_running[0]:
            sw_elapsed[0] += time.time() - sw_start_time[0]
            sw_running[0] = False

    def reset_sw():
        sw_running[0] = False
        sw_elapsed[0] = 0
        sw_display.config(text="00:00:00")

    sw_buttons = tk.Frame(sw, bg="#1e1e1e")
    sw_buttons.pack()

    tk.Button(sw_buttons, text="Start", command=start_sw, bg="green", fg="white", width=8).grid(row=0, column=0, padx=5)
    tk.Button(sw_buttons, text="Stop", command=stop_sw, bg="red", fg="white", width=8).grid(row=0, column=1, padx=5)
    tk.Button(sw_buttons, text="Reset", command=reset_sw, bg="gray", fg="white", width=8).grid(row=0, column=2, padx=5)


def open_timer():
    tm = tk.Toplevel(root)
    tm.title("Timer")
    tm.geometry("350x320")
    tm.config(bg="#1e1e1e")

    tm_display = tk.Label(tm, text="00:00:00", font=("Courier", 30), fg="cyan", bg="black", width=10, bd=3, relief="sunken")
    tm_display.pack(pady=20)

    h = [0]
    m = [0]
    s = [0]

    def format_tm(t):
        m_ = int(t // 60)
        s_ = int(t % 60)
        ms = int((t - int(t)) * 100)
        return f"{m_:02}:{s_:02}:{ms:02}"

    tm_running = [False]
    tm_target = [0]
    tm_start = [0]

    def update_tm():
        if tm_running[0]:
            left = tm_target[0] - (time.time() - tm_start[0])
            if left <= 0:
                tm_display.config(text="00:00:00")
                tm_running[0] = False
                messagebox.showinfo("Time Up", "Timer finished!")
            else:
                tm_display.config(text=format_tm(left))
                tm.after(10, update_tm)

    def start_tm():
        total = h[0]*3600 + m[0]*60 + s[0]
        if total == 0:
            messagebox.showerror("Error", "Set a valid time.")
            return
        tm_target[0] = total
        tm_start[0] = time.time()
        tm_running[0] = True
        update_tm()

    def stop_tm():
        tm_running[0] = False

    def reset_tm():
        tm_running[0] = False
        tm_display.config(text="00:00:00")

    def inc(var, label, unit):
        var[0] += 1
        if unit == "m" or unit == "s":
            if var[0] > 59:
                var[0] = 0
        label.config(text=f"{var[0]:02}")

    def dec(var, label, unit):
        if var[0] > 0:
            var[0] -= 1
        else:
            if unit == "m" or unit == "s":
                var[0] = 59
        label.config(text=f"{var[0]:02}")

    set_frame = tk.Frame(tm, bg="#1e1e1e")
    set_frame.pack(pady=10)

    def make_counter(col, var, text, unit):
        frame = tk.Frame(set_frame, bg="#1e1e1e")
        frame.grid(row=0, column=col, padx=10)
        tk.Label(frame, text=text, fg="white", bg="#1e1e1e").pack()
        val_label = tk.Label(frame, text="00", font=("Courier", 20), fg="yellow", bg="#1e1e1e")
        val_label.pack()
        tk.Button(frame, text="▲", width=3, command=lambda: inc(var, val_label, unit)).pack(pady=2)
        tk.Button(frame, text="▼", width=3, command=lambda: dec(var, val_label, unit)).pack()
        return val_label

    make_counter(0, h, "H", "h")
    make_counter(1, m, "M", "m")
    make_counter(2, s, "S", "s")

    btns = tk.Frame(tm, bg="#1e1e1e")
    btns.pack(pady=20)

    tk.Button(btns, text="Start", command=start_tm, bg="green", fg="white", width=10).grid(row=0, column=0, padx=5)
    tk.Button(btns, text="Stop", command=stop_tm, bg="red", fg="white", width=10).grid(row=0, column=1, padx=5)
    tk.Button(btns, text="Reset", command=reset_tm, bg="gray", fg="white", width=10).grid(row=0, column=2, padx=5)

root = tk.Tk()
root.title("Timer & Stopwatch")
root.geometry("300x200")
root.config(bg="#121212")

tk.Label(root, text="Select Mode", font=("Helvetica", 16), fg="white", bg="#121212").pack(pady=20)
tk.Button(root, text="Stopwatch", command=open_stopwatch, width=20, bg="blue", fg="white", font=("Helvetica", 12)).pack(pady=10)
tk.Button(root, text="Timer", command=open_timer, width=20, bg="purple", fg="white", font=("Helvetica", 12)).pack(pady=10)

root.mainloop()
