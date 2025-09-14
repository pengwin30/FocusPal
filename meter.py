import ttkbootstrap as ttk
from ttkbootstrap.constants import *

app = ttk.Window()

meter = ttk.Meter(
    metersize=180,
    padding=5,
    amountused=25,
    metertype="full",
    subtext="miles per hour",
    interactive=False,
    arcrange=100,
    stripethickness=10,
    # meterstyle='%',
    # textleft='45',
    textright='%',
    bootstyle='info'
)
meter.pack()

# update the amount used directly
meter.configure(amountused = 50)
# meter.configure(meterstyle = '%')


# increment the amount by 10 steps
meter.step(10)

# decrement the amount by 15 steps
meter.step(-15)

# update the subtext
# meter.configure(subtext="loading...")

app.mainloop()