# Implementation using purely ttkbootstrap

import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from PIL import Image, ImageTk

import time
from datetime import datetime, timedelta

# <----------------- ROOT ----------------->
root = ttk.Window(themename="minty")
# These are methods, we call them directly without using configure()
root.geometry('350x400')
root.title("FocusPal")
root.resizable(False, False)

# <----------------- CONTAINER (For Frame Switching) ----------------->
# Create Container Frame
# style = ttk.Style()
# style.configure('custom.Container', background='lightblue', relief='flat')
container = ttk.Frame(root)
container.pack(fill="both", expand=True)

# Make grid inside container expandable
container.rowconfigure(0, weight=1)
container.columnconfigure(0, weight=1)



# <----------------- MAIN PAGE ----------------->
# Page: Main Page
style = ttk.Style()
style.configure('MainPage.TFrame', background="#C8FFFC", relief='flat')
# MainPage = ttk.Frame(container, style='MainPage.TFrame')
MainPage = ttk.Frame(container)
MainPage.grid(row=0, column=0, sticky="nsew")
# MainPage.grid(row=0, column=0, sticky="nsew")

# Grid (1x2)
MainPage.columnconfigure(0, weight=1)
MainPage.columnconfigure(1, weight=1)
MainPage.rowconfigure(0, weight=1)
MainPage.rowconfigure(1, weight=3)



# Text widget
style = ttk.Style()
# style.configure('Title.TLabel', foreground='black', background='lightblue', relief='flat', font=("Cascadia Mono SemiBold", 24, "bold"))
style.configure('Title.TLabel', foreground='black', relief='flat', font=("Cascadia Mono SemiBold", 24, "bold"))
label = ttk.Label(MainPage, text='FocusPal', style='Title.TLabel')
label.grid(column=0, columnspan=2, row=0, padx=15, pady=15)



def timer(minutes: int):
    worktime = int(0.9 * minutes)
    resttime = minutes - worktime
    start_time = datetime.now()

    def work_update():
        minutes_elapsed = int((datetime.now() - start_time).total_seconds() / 60)
        percentage = int((minutes_elapsed / worktime) * 100)
        meter.configure(amountused=percentage)

        if percentage < 100:
            meter.after(1000, work_update)
        else:
            pmd_label.configure(text="Work done! Starting rest...")
            start_rest()

    def start_rest():
        rest_start = datetime.now()

        def rest_update():
            minutes_elapsed = int((datetime.now() - rest_start).total_seconds() / 60)
            percentage = int((minutes_elapsed / resttime) * 100)
            meter.configure(amountused=percentage)

            if percentage < 100:
                meter.after(1000, rest_update)
            else:
                pmd_label.configure(text="Rest complete! Back to work?")

        rest_update()

    work_update()

# <----------------- MAIN PAGE: BUTTON 1 ----------------->
def pomodoro():
    PomodoroPage.tkraise()
    timer(3)











style = ttk.Style()
# style.configure(
#     'MainButton.TButton',
#     # background="#8CE292",
#     bordercolor='black',
#     compound=ttk.TOP,
#     # darkcolor="#B6FFBB",
#     # focuscolor='black',
#     # focusthickness=2,
#     foreground='black',
#     font=("Helvetica", 18),
#     # lightcolor="#D6FFD8",
#     relief='ridge',
#     # padding=(0, 20),
#     width=100
# )
# Copy options from info.TButton into MainButton.TButton
style.configure("MainButton.TButton", **style.configure("light.TButton"))

# Now override only what you need
style.configure(
    "MainButton.TButton",
    font=("Cascadia Mono SemiBold", 20, "bold"),
    foreground="black",  # only if you want to override
    relief="ridge",
    width=100
)


# Create a styled button
PomodoroIconOriginal = Image.open('./assets/pomodoro_tomato.png')
PomodoroIconResized = PomodoroIconOriginal.resize((100,100))
PomodoroIcon = ImageTk.PhotoImage(PomodoroIconResized)

# Both tkinter and tkinter.ttk have Button widget.
# tkinter.ttk.Button does not support font option.

PomBtn = ttk.Button(
    MainPage,
    text="Pomodoro",
    image=PomodoroIcon,
    style="MainButton.TButton",
    compound="top",  # show text under icon
    command=pomodoro
)


PomBtn.grid(
    column=0,
    row=1,
    # ipadx=50,
    # ipady=50,
    padx=10,
    pady=10,
    sticky='N'
)


# <----------------- MAIN PAGE: BUTTON 2 ----------------->
# Button 2:
def trading():
    # showinfo(
    #     title='Information',
    #     message='Pomodoro time!'
    # )
    return 0



# Create a styled button
TradingIconOriginal = Image.open('./assets/stock_market.png')
TradingIconResized = TradingIconOriginal.resize((100,100))
TradingIcon = ImageTk.PhotoImage(TradingIconResized)

TBtn = ttk.Button(
    MainPage,
    text="Trading",
    image=TradingIcon,
    style='MainButton.TButton',
    compound="top",
    command=trading,   # Since I declared text before image, this compound is for image relative to text.
)
TBtn.grid(
    column=1,
    row=1,
    # ipadx=50,
    # ipady=50,
    padx=10,
    pady=10,
    sticky='N'
)




# <----------------- POMODORO PAGE ----------------->
# Page: POMODORO Page
style = ttk.Style()
style.configure('Pomodoro.TFrame', relief='flat')           # Removed background colour to match with Meter
PomodoroPage = ttk.Frame(container, style='Pomodoro.TFrame')
PomodoroPage.grid(row=0, column=0, sticky="nsew")


# Grid (1x2)
PomodoroPage.columnconfigure(0, weight=1)
PomodoroPage.rowconfigure(0, weight=1)
PomodoroPage.rowconfigure(1, weight=2)
PomodoroPage.rowconfigure(2, weight=1)



# Text widget
style = ttk.Style()
style.configure('Pomodoro.TLabel', foreground='black', relief='flat', font=("Cascadia Mono SemiBold", 24, "bold"))
label = ttk.Label(PomodoroPage, text='Pomodoro', style='Pomodoro.TLabel')
label.grid(column=0, row=0)


meter = ttk.Meter(
    PomodoroPage,
    metersize=220,
    # padding=5,
    # amountused=25,
    metertype="full",
    subtext="Beat it!",
    interactive=False,
    arcrange=360,
    stripethickness=10,
    # meterstyle='%',
    # textleft='45',
    textright='%',
    bootstyle=SECONDARY
)
meter.grid(column=0, row=1)

# update the amount used directly
# meter.configure(amountused = 50)

# increment the amount by 10 steps
# meter.step(10)



# Text widget
style = ttk.Style()
style.configure('Meter.TLabel', foreground='black', relief='flat', font=("Cascadia Mono SemiBold", 12, "bold"))
pmd_label = ttk.Label(PomodoroPage, text='Session #1', style='Meter.TLabel')
pmd_label.grid(column=0, row=2, padx=15, pady=15)







MainPage.tkraise()

root.mainloop()