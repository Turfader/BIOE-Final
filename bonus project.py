
from package_installer import install
try:
    import ntplib
except ModuleNotFoundError:
    install()
finally:
    import nntplib

from datetime import datetime

print("fetching datetime")

ntp_client = ntplib.NTPClient()
ntp_server = 'time.windows.com'

try:
    response = ntp_client.request(ntp_server)
    current_time = response.tx_time
    current_datetime = datetime.fromtimestamp(current_time)
    print("Current time: ", current_datetime)

    print("Displaying in window")
    import tkinter as tk
    from tkinter import messagebox

    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("Current Time", current_datetime)


except Exception as e:
    print(e)
