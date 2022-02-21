from tkinter import *
import webbrowser
import os

# https://sky.shiiyu.moe/stats/BurnDownTheWorld/Kiwi

root = Tk()
root.title("Hypixel SB Stat Checker")
root.resizable(False, False)

currentlocation = os.path.dirname(os.path.abspath(__file__))

navbar = Menu(root)
root.config(menu=navbar)

other_stats_menu = Menu(navbar)
navbar.add_cascade(label="Other Stat Trackers", menu=other_stats_menu)
other_stats_menu.add_command(label="Fortnite", command=lambda: fortnite())
other_stats_menu.add_command(label="Hypixel", command=lambda: hypixel())
other_stats_menu.add_command(label="Valorant", command=lambda: valorant())

def fortnite():
    os.system(f'C:/Python38/python.exe "{currentlocation}/fortnite_stat_tracker.pyw"')

def hypixel():
    os.system(f'C:/Python38/python.exe "{currentlocation}/hypixel_stat_tracker.pyw"')

def valorant():
    os.system(f'C:/Python38/python.exe "{currentlocation}/val_stat_tracker.pyw"')


def searchbtn():
    global namebox, profilebox
    ign = namebox.get(1.0, "end-1c")
    profile = profilebox.get(1.0, "end-1c")
    link = f"https://sky.shiiyu.moe/stats/{ign}/{profile}"
    linkbtn = Button(root, text="View Stats", height=1,width=20,command=lambda: openStats(link))
    linkbtn.place(y=290,x=190)


def openStats(link):
    webbrowser.open_new(link)



window_height = 325
window_width = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

namebox = Text(root, height=2, width=25)
namebox.place(y=100,x=100)
nameboxtitle = Label(root, text="Name", font=("helvetica",10))
nameboxtitle.place(y=70,x=175)

profilebox = Text(root, height=2, width=10)
profilebox.place(y=100,x=350)
profileboxtitle = Label(root, text="Profile", font=("helvetica", 10))
profileboxtitle.place(y=70,x=375)

searchforplayerbutton = Button(root, text="Search For Player Stats", height=1, width=25, bg="SystemButtonFace", command=lambda: searchbtn())
searchforplayerbutton.place(y=250,x=175)



root.mainloop()