import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from PIL import Image, ImageTk

# <----------------- ROOT ----------------->
root = ttk.Window(themename="morph")
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
style.configure('MainPage.TFrame', background='lightblue', relief='flat')
MainPage = ttk.Frame(container, style='MainPage.TFrame')
MainPage.grid(row=0, column=0, sticky="nsew")
# MainPage.grid(row=0, column=0, sticky="nsew")

# Grid (1x2)
MainPage.columnconfigure(0, weight=1)
MainPage.columnconfigure(1, weight=1)
MainPage.rowconfigure(0, weight=1)
MainPage.rowconfigure(1, weight=3)



# Text widget
style = ttk.Style()
style.configure('Title.TLabel', foreground='black', background='lightblue', relief='flat', font=("Cascadia Mono SemiBold", 24, "bold"))
label = ttk.Label(MainPage, text='FocusPal', style='Title.TLabel')
label.grid(column=0, columnspan=2, row=0, padx=15, pady=15)





# <----------------- MAIN PAGE: BUTTON 1 ----------------->
def pomodoro():
    PomodoroPage.tkraise()

style = ttk.Style()
style.configure(
    'MainButton.TButton',
    background="#45a049",
    bordercolor='black',
    compound=ttk.TOP,
    darkcolor="#246428",
    # focuscolor='black',
    # focusthickness=2,
    foreground='black',
    font=("Helvetica", 18),
    lightcolor="#6dc271",
    relief='ridge',
    # padding=(0, 20),
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
    style='MainButton.TButton',
    command=pomodoro   # Since I declared text before image, this compound is for image relative to text.
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


style = ttk.Style()
style.configure(
    'MainButton.TButton',
    background="#45a049",
    bordercolor='black',
    compound=ttk.TOP,
    darkcolor="#246428",
    # focuscolor='black',
    # focusthickness=2,
    foreground='black',
    font=("Cascadia Mono SemiBold", 20, "bold"),
    lightcolor="#6dc271",
    relief='ridge',
    # padding=(0, 20),
    width=130
)

# Create a styled button
TradingIconOriginal = Image.open('./assets/stock_market.png')
TradingIconResized = TradingIconOriginal.resize((100,100))
TradingIcon = ImageTk.PhotoImage(TradingIconResized)

TBtn = ttk.Button(
    MainPage,
    text="Trading",
    image=TradingIcon,
    style='MainButton.TButton',
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
label.grid(column=0, row=0, padx=15, pady=15)


meter = ttk.Meter(
    PomodoroPage,
    metersize=180,
    # padding=5,
    amountused=25,
    metertype="full",
    subtext="miles per hour",
    interactive=False,
    arcrange=100,
    stripethickness=10,
    # meterstyle='%',
    # textleft='45',
    textright='%',
    bootstyle=DARK
)
meter.grid(column=0, row=1, padx=10, pady=10)

# update the amount used directly
meter.configure(amountused = 50)

# increment the amount by 10 steps
meter.step(10)



# Text widget
style = ttk.Style()
style.configure('Meter.TLabel', foreground='black', relief='flat', font=("Cascadia Mono SemiBold", 12, "bold"))
label = ttk.Label(PomodoroPage, text='Pomodoro', style='Meter.TLabel')
label.grid(column=0, row=2, padx=15, pady=15)







MainPage.tkraise()

root.mainloop()