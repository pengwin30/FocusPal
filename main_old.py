import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import font as tkFont

from PIL import Image, ImageTk


# <----------------- ROOT ----------------->
# tk.Tk() does not accept keyword arguments.
root = tk.Tk()
# These are methods, we call them directly without using configure()
root.geometry('320x370')
root.title("FocusPal")
root.resizable(False, False)
# bg is option, so we use configure()
root.configure(bg='lightblue')     # set background color


# <----------------- CONTAINER (For Frame Switching) ----------------->
# Create container
container = tk.Frame(root)
container.pack(fill="both", expand=True)

# Make grid inside container expandable
container.rowconfigure(0, weight=1)
container.columnconfigure(0, weight=1)


# <----------------- MAIN PAGE ----------------->
# Page: Main Page
MainPage = tk.Frame(container, bg="lightblue")
MainPage.grid(row=0, column=0, sticky="nsew")

# Grid (1x2)
MainPage.columnconfigure(0, weight=1)
MainPage.columnconfigure(1, weight=1)
MainPage.rowconfigure(0, weight=1)
MainPage.rowconfigure(1, weight=3)

# Text widget
label = ttk.Label(
    MainPage,
    text='FocusPal',
    font=("Cascadia Mono SemiBold", 24, "bold"),
    background='lightblue'
)
label.grid(
    column=0,
    columnspan=2,
    row=0,
    # ipadx=50,
    # ipady=50,
    padx=15,
    pady=15,
    # sticky='NW'
)

# <----------------- MAIN PAGE: BUTTON 1 ----------------->
# Button 1: 
def pomodoro():
    PomodoroPage.tkraise()

# Create a styled button
PomodoroIconOriginal = Image.open('./assets/pomodoro_tomato.png')
PomodoroIconResized = PomodoroIconOriginal.resize((100,100))
PomodoroIcon = ImageTk.PhotoImage(PomodoroIconResized)

# Both tkinter and tkinter.ttk have Button widget.
# tkinter.ttk.Button does not support font option.
PomBtn = tk.Button(
    MainPage,
    text="Pomodoro",
    image=PomodoroIcon,
    compound=tk.TOP,
    command=pomodoro,   # Since I declared text before image, this compound is for image relative to text.
    font=("Cascadia Mono SemiBold", 16, "bold"),
    fg="black",                   # Text color
    bg="#45a049",                 # Background color (green)
    activebackground="#FFB84D",   # Background when pressed
    activeforeground="white",     # Text color when pressed
    relief="ridge",                # Flat style (cleaner than raised)
    bd=4,                         # No border,
    width=130,
    height=150
)
PomBtn.grid(
    column=0,
    row=1,
    # ipadx=50,
    # ipady=50,
    padx=15,
    pady=15,
    sticky='N'
)
# btn.pack(
#     ipadx=8,       # These pads are added between the button borders and inside contents.
#     ipady=8,        # "Internal" Pad
#     expand=True,
#     # side=tk.TOP,
#     # padx=10,
#     # pady=10
# )

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

TBtn = tk.Button(
    MainPage,
    text="Trading",
    image=TradingIcon,
    compound=tk.TOP,
    command=trading,   # Since I declared text before image, this compound is for image relative to text.
    font=("Cascadia Mono SemiBold", 16, "bold"),
    fg="black",                   # Text color
    bg="#45a049",                 # Background color (green)
    activebackground="#FFB84D",   # Background when pressed
    activeforeground="white",     # Text color when pressed
    relief="ridge",                # Flat style (cleaner than raised)
    bd=4,                         # No border
    width=130,
    height=150
)
TBtn.grid(
    column=1,
    row=1,
    # ipadx=50,
    # ipady=50,
    padx=15,
    pady=15,
    sticky='N'
)










# <----------------- POMODORO PAGE ----------------->
# Page: Pomodoro Page
PomodoroPage = tk.Frame(container, bg="lightyellow")
PomodoroPage.grid(row=0, column=0, sticky="nsew")



MainPage.tkraise()
# root.mainloop() starts Tkinter's event loop, waiting for and handling user actions (not re-running the code).
root.mainloop()












