from tkinter import *
import webbrowser
import os
from tkinter import messagebox


# https://sky.shiiyu.moe/stats/BurnDownTheWorld/Kiwi

currentlocation = os.path.dirname(os.path.abspath(__file__))

root = Tk()
root.title("Hypixel SB Stat Checker")
root.resizable(False, False)
root.overrideredirect(True)
root.geometry("500x325")
root.attributes("-topmost",1)


def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb

root.config(bg=rgb_hack((41, 41, 41)))


def fortnite():
    os.system(f'C:/Python38/python.exe "{currentlocation}/fortnite_stat_tracker.pyw"')

def hypixel():
    os.system(f'C:/Python38/python.exe "{currentlocation}/hypixel_stat_tracker.pyw"')

def valorant():
    os.system(f'C:/Python38/python.exe "{currentlocation}/val_stat_tracker.pyw"')


def searchandopen():
    global namebox, profilebox
    ign = namebox.get(1.0, "end-1c")
    profile = profilebox.get(1.0, "end-1c")
    if len(ign) >= 4:
        if len(profile) >= 4:
            link = f"https://sky.shiiyu.moe/stats/{ign}/{profile}"
            webbrowser.open_new(link)
            #showstats(link)
        else:
            messagebox.showinfo("ERROR", "Not Enough Info Provided")
    else:
        messagebox.showinfo("ERROR", "Not Enough Info Provided")



def showcredits():
    creditwindow = Tk()
    creditwindow.title("Credits")

    window_height = 400
    window_width = 425

    screen_width = creditwindow.winfo_screenwidth()
    screen_height = creditwindow.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    creditwindow.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    mitchell = Label(creditwindow, text="Made By Mitchell Gibbons AKA", fg="white", bg="black")
    burndowntheworld = Label(creditwindow, text="Burndowntheworld", fg="white", bg="black")
    discord = Label(creditwindow, text="burndowntheworld#6969", fg="white", bg="black")
    email = Label(creditwindow, text="burndowntheworld1@gmail.com", fg="white", bg="black")


    copyrightwarning = Label(creditwindow, text="Current form of our 'valorant stat tracker' app is subject to change due to copyright strikes.", font=("helvetica",7), fg="white", bg="black")
    trackerggcredit = Label(creditwindow, text="All Statistics' data pulled from tracker.gg.", font=("helvetica",7), fg="white", bg="black")
    notpartneredwithtrackergg = Label(creditwindow, text="We are not affiliated, or partnered with 'Tracker Network'. We do not work for/with 'Tracker Network'.", font=("helvetica",7), fg="white", bg="black")
    

    mitchell.pack(pady=(100,0))
    burndowntheworld.pack()
    discord.pack()
    email.pack()

    trackerggcredit.pack(anchor="sw", pady=(155,0))
    notpartneredwithtrackergg.pack(anchor="sw")
    copyrightwarning.pack(anchor="sw")


    creditwindow.resizable(False, False)
    creditwindow.overrideredirect(1)
    creditwindow.attributes("-topmost", "1")
    creditwindow.configure(bg='black')

    creditsclosebutton = Button(creditwindow, text="X", height=1, width=1, bg="black", fg="white", command=lambda: creditwindow.destroy())
    creditsclosebutton.place(y=5, x=400)


def openinbrowser(link):
    webbrowser.open_new(link)


def duosplit(string):
    words = string.split()
    grouped_words = [' '.join(words[i: i + 2]) for i in range(0, len(words), 2)]
    return grouped_words


def nothing():
    pass


def move(e):
    root.geometry(f"+{e.x_root}+{e.y_root}")


def openotherappsmenu():
    otherapps.pack_forget()
    othermenu.pack_forget()
    
    global fortnitel, hypixell, valorantl, otherappsbackl

    fortnitel = Label(menubar, text="Fortnite", bg="MediumOrchid4", fg="white")
    fortnitel.pack(side=LEFT, padx=20)
    fortnitel.bind('<Button-1>',lambda f: fortnite())

    hypixell = Label(menubar, text="Hypixel", bg="MediumOrchid4", fg="white")
    hypixell.pack(side=LEFT, padx=(0,20))
    hypixell.bind('<Button-1>', lambda h: hypixel())

    valorantl = Label(menubar, text="Valorant", bg="MediumOrchid4", fg="white")
    valorantl.pack(side=LEFT, padx=(0,20))
    valorantl.bind('<Button-1>', lambda v: valorant())

    otherappsbackl = Label(menubar, text="Back", bg="MediumOrchid4", fg="white")
    otherappsbackl.pack(side=LEFT, padx=(0,20))
    otherappsbackl.bind('<Button-1>', lambda b: otherappsmenuback())


def otherappsmenuback():
    fortnitel.pack_forget()
    hypixell.pack_forget()
    valorantl.pack_forget()
    otherappsbackl.pack_forget()
    defaultmenu()



def openothermenumenu():
    otherapps.pack_forget()
    othermenu.pack_forget()

    global creditsl, othermenubackl

    creditsl = Label(menubar, text="Credits", bg="MediumOrchid4", fg="white")
    creditsl.pack(side=LEFT, padx=20)
    creditsl.bind('<Button-1>',lambda c: showcredits())

    othermenubackl = Label(menubar, text="Back", bg="MediumOrchid4", fg="white")
    othermenubackl.pack(side=LEFT, padx=(0,20))
    othermenubackl.bind('<Button-1>',lambda b: othermenuback())



def othermenuback():
    creditsl.pack_forget()
    othermenubackl.pack_forget()
    defaultmenu()



def defaultmenu():
    global otherapps, valorantextras, othermenu
    otherapps = Label(menubar, text="Other Stat Trackers", bg="MediumOrchid4", fg="white")
    otherapps.pack(side=LEFT, padx=20)
    otherapps.bind('<Button-1>',lambda s: openotherappsmenu())

    othermenu = Label(menubar, text="Other", bg="MediumOrchid4", fg="white")
    othermenu.pack(side=LEFT, padx=(0,20))
    othermenu.bind('<Button-1>', lambda o: openothermenumenu())




namebox = Text(root, height=2, width=25, bg=rgb_hack((100, 100, 100)), fg="white")
namebox.place(y=100,x=100)
nameboxtitle = Label(root, text="Name", font=("helvetica",10), bg=rgb_hack((41, 41, 41)), fg="white")
nameboxtitle.place(y=70,x=175)

profilebox = Text(root, height=2, width=10, bg=rgb_hack((100, 100, 100)), fg="white")
profilebox.place(y=100,x=350)
profileboxtitle = Label(root, text="Profile", font=("helvetica", 10), bg=rgb_hack((41, 41, 41)), fg="white")
profileboxtitle.place(y=70,x=375)

searchforplayerbutton = Button(root, text="Search For Player Stats", height=1, width=25, bg=rgb_hack((100, 100, 100)), fg="white", command=lambda: searchandopen())
searchforplayerbutton.place(y=200,x=175)

title_bar = Frame(root, bg=rgb_hack((80, 80, 80)), relief="raised", bd=0)
title_bar.pack(expand=1, fill=X, anchor="nw")
title_bar.bind('<B1-Motion>', move)


title_bar_title = Label(title_bar, text="Hypixel Skyblock Stat Tracker", bg=rgb_hack((80,80,80)),bd=0,fg='white',font=("helvetica", 10),highlightthickness=0)
title_bar_title.pack(side=LEFT, pady=6, padx=(10,0))


close_button = Button(title_bar, text='  ×  ', command=root.destroy,bg=rgb_hack((80, 80, 80)),padx=2,pady=2,font=("calibri", 13),bd=0,fg='white',highlightthickness=0)
close_button.pack(side=RIGHT)


menubar = Frame(root, bg="Orchid4", borderwidth=2, relief="ridge", highlightcolor="purple2")
menubar.pack(expand=1, fill=X, anchor="s")

menubartitle = Label(menubar, text="    MENU    ", bg="Orchid4", fg="white")
menubartitle.pack(side=LEFT, pady=(15,15))


otherapps = Label(menubar, text="Other Stat Trackers", bg="MediumOrchid4", fg="white")
otherapps.pack(side=LEFT, padx=20)
otherapps.bind('<Button-1>',lambda s: openotherappsmenu())


othermenu = Label(menubar, text="Other", bg="MediumOrchid4", fg="white")
othermenu.pack(side=LEFT, padx=(0,20))
othermenu.bind('<Button-1>', lambda o: openothermenumenu())


root.mainloop()
