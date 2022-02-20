from tkinter import *
import webbrowser
import os
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
from tkinter import ttk
from PIL import Image, ImageTk


root = Tk()
root.title("Valorant Stat Checker")
root.resizable(False, False)
root.iconphoto(False, PhotoImage(file='/Users/mgibbons/Desktop/game stat checkers/valorant.png'))
root.overrideredirect(True)
root.geometry("500x325")
root.attributes("-topmost",1)


def rgb_hack(rgb):
    return "#%02x%02x%02x" % rgb

root.config(bg=rgb_hack((41, 41, 41)))



def fortnite():
    os.system('C:/Python38/python.exe "c:/Users/mgibbons/Desktop/game stat checkers/fortnite stat tracker.pyw"')

def hypixel():
    os.system('C:/Python38/python.exe "c:/Users/mgibbons/Desktop/game stat checkers/hypixel stat tracker.pyw"')

def hypixelsb():
    os.system('C:/Python38/python.exe "c:/Users/mgibbons/Desktop/game stat checkers/hypixel sb stat checker.pyw"')



def agents():
    webbrowser.open_new("https://tracker.gg/valorant/agents")

def weapons():
    webbrowser.open_new("https://tracker.gg/valorant/weapons")

def maps():
    webbrowser.open_new("https://tracker.gg/valorant/maps")

def cards():
    webbrowser.open_new("https://tracker.gg/valorant/cards")

def buddies():
    webbrowser.open_new("https://tracker.gg/valorant/buddies")

def sprays():
    webbrowser.open_new("https://tracker.gg/valorant/sprays")


def searchandopen():
    global namebox, tagbox
    tag = tagbox.get(1.0, "end-1c")
    name = namebox.get(1.0, "end-1c")
    if len(name) >= 4:
        if len(tag) >= 3:
            link = f"https://tracker.gg/valorant/profile/riot/{name}%23{tag}/overview"
            #webbrowser.open_new(link)
            showstats(link)
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



def showstats(link):
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html5lib')
    try:
        kad = soup.find('span', attrs = {'class':'valorant-highlighted-stat__value'})
        kad = kad.get_text()
        playtime = soup.find('span', attrs = {'class':'playtime'})
        playtime = playtime.get_text()
        games_played = soup.find('span', attrs = {'class':'matches'})
        games_played = games_played.get_text()
        otherdata = soup.find('div', attrs = {'class':'main'})
        otherdata = otherdata.get_text()
        listofotherstats = duosplit(otherdata)
        wins = listofotherstats[0]
        kills = listofotherstats[1]
        headshots = listofotherstats[2]
        deaths = listofotherstats[3]
        assists = listofotherstats[4]
        scoreperround = listofotherstats[5]
        killsperround = listofotherstats[6]
        topagentslist = []
        for tr in soup.find_all('tr')[1:]:
            tds = tr.find_all('td')
            topagentslist.append(tds[0].text)
            
        topagents = f"""
        your top agents are:
        1.{topagentslist[0]}
        2.{topagentslist[1]}
        3.{topagentslist[2]}
        """


        statswindow = Tk()
        statswindow.title("Stats Overview")
        

        window_height = 1000
        window_width = 600

        screen_width = statswindow.winfo_screenwidth()
        screen_height = statswindow.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        statswindow.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        statswindow.resizable(False, False)
        statswindow.overrideredirect(1)
        statswindow.attributes("-topmost", "1")
        statswindow.configure(bg=rgb_hack((41, 41, 41)))

        kadlabel = Label(statswindow, text=f"kad ratio {kad}", fg="white", bg=rgb_hack((41, 41, 41)), font=("helvetica", 18))
        playtimelabel = Label(statswindow, text=f"you have {playtime}", fg="white", bg=rgb_hack((41, 41, 41)), font=("helvetica", 18))
        gamesplayedlabel = Label(statswindow, text=f"you have played {games_played}", fg="white", bg=rgb_hack((41, 41, 41)), font=("helvetica", 18))
        winslabel = Label(statswindow, text=wins, fg="white", bg=rgb_hack((41, 41, 41)), font=("helvetica", 18))
        killslabel = Label(statswindow, text=kills, fg="white", bg=rgb_hack((41, 41, 41)), font=("helvetica", 18))
        headshotslabel = Label(statswindow, text=headshots, fg="white", bg=rgb_hack((41, 41, 41)), font=("helvetica", 18))
        deathslabel = Label(statswindow, text=deaths, fg="white", bg=rgb_hack((41, 41, 41)), font=("helvetica", 18))
        assistslabel = Label(statswindow, text=assists, fg="white", bg=rgb_hack((41, 41, 41)), font=("helvetica", 18))
        scoreperroundlabel = Label(statswindow, text=scoreperround, fg="white", bg=rgb_hack((41, 41, 41)), font=("helvetica", 18))
        killsperroundlabel = Label(statswindow, text=killsperround, fg="white", bg=rgb_hack((41, 41, 41)), font=("helvetica", 18))
        topagentslabel = Label(statswindow, text=topagents, fg="white", bg=rgb_hack((41, 41, 41)), font=("helvetica", 18))

        kadlabel.place(y=10,x=20)
        playtimelabel.place(y=700,x=0)
        gamesplayedlabel.place(y=850,x=20)
        winslabel.place(y=100,x=20)
        killslabel.place(y=130,x=20)
        headshotslabel.place(y=160,x=20)
        deathslabel.place(y=190,x=20)
        assistslabel.place(y=220,x=20)
        scoreperroundlabel.place(y=250,x=20)
        killsperroundlabel.place(y=280,x=20)
        topagentslabel.place(y=400,x=0)



        statswindowclosebutton = Button(statswindow, text="X", height=1, width=1, bg=rgb_hack((41, 41, 41)), fg="white", command=lambda: statswindow.destroy())
        statswindowclosebutton.place(y=5, x=575)

        openinbrowserbutton = Button(statswindow, text="open original in browser", bg=rgb_hack((100, 100, 100)), fg="white", command=lambda: openinbrowser(link))
        openinbrowserbutton.place(y=900, x=400)


    except:
        messagebox.showinfo("ERROR","Something went wrong. Try another account.")



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
    valorantextras.pack_forget()

    global fortnitel, hypixell, hypixelsbl, otherappsbackl

    fortnitel = Label(menubar, text="Fortnite", bg="MediumOrchid4", fg="white")
    fortnitel.pack(side=LEFT, padx=20)
    fortnitel.bind('<Button-1>',lambda f: fortnite())

    hypixell = Label(menubar, text="Hypixel", bg="MediumOrchid4", fg="white")
    hypixell.pack(side=LEFT, padx=(0,20))
    hypixell.bind('<Button-1>', lambda h: hypixel())

    hypixelsbl = Label(menubar, text="Hypixel SB", bg="MediumOrchid4", fg="white")
    hypixelsbl.pack(side=LEFT, padx=(0,20))
    hypixelsbl.bind('<Button-1>', lambda hsb: hypixelsb())

    otherappsbackl = Label(menubar, text="Back", bg="MediumOrchid4", fg="white")
    otherappsbackl.pack(side=LEFT, padx=(0,20))
    otherappsbackl.bind('<Button-1>', lambda b: otherappsmenuback())



def otherappsmenuback():
    fortnitel.pack_forget()
    hypixell.pack_forget()
    hypixelsbl.pack_forget()
    otherappsbackl.pack_forget()
    defaultmenu()



def openvalorantextrasmenu():
    otherapps.pack_forget()
    othermenu.pack_forget()
    valorantextras.pack_forget()

    global agentsl, weaponsl, mapsl, cardsl, buddiesl, spraysl, valorantextrasbackl

    agentsl = Label(menubar, text="Agents", bg="MediumOrchid4", fg="white")
    agentsl.pack(side=LEFT, padx=18)
    agentsl.bind('<Button-1>',lambda a: agents())

    weaponsl = Label(menubar, text="Weapons", bg="MediumOrchid4", fg="white")
    weaponsl.pack(side=LEFT, padx=(0,18))
    weaponsl.bind('<Button-1>',lambda w: weapons())

    mapsl = Label(menubar, text="Maps", bg="MediumOrchid4", fg="white")
    mapsl.pack(side=LEFT, padx=(0,18))
    mapsl.bind('<Button-1>',lambda m: maps())


    cardsl = Label(menubar, text="Cards", bg="MediumOrchid4", fg="white")
    cardsl.pack(side=LEFT, padx=(0,18))
    cardsl.bind('<Button-1>',lambda c: cards())

    buddiesl = Label(menubar, text="Buddies", bg="MediumOrchid4", fg="white")
    buddiesl.pack(side=LEFT, padx=(0,18))
    buddiesl.bind('<Button-1>',lambda b: buddies())

    spraysl = Label(menubar, text="Sprays", bg="MediumOrchid4", fg="white")
    spraysl.pack(side=LEFT, padx=(0,18))
    spraysl.bind('<Button-1>',lambda s: sprays())

    valorantextrasbackl = Label(menubar, text="Back", bg="MediumOrchid4", fg="white")
    valorantextrasbackl.pack(side=LEFT, padx=(0,20))
    valorantextrasbackl.bind('<Button-1>', lambda b: valorantextrasback())


def valorantextrasback():
    agentsl.pack_forget()
    weaponsl.pack_forget()
    mapsl.pack_forget()
    cardsl.pack_forget()
    buddiesl.pack_forget()
    spraysl.pack_forget()
    valorantextrasbackl.pack_forget()
    defaultmenu()



def openothermenumenu():
    otherapps.pack_forget()
    othermenu.pack_forget()
    valorantextras.pack_forget()

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

    valorantextras = Label(menubar, text="Valorant Extras", bg="MediumOrchid4", fg="white")
    valorantextras.pack(side=LEFT, padx=(0,20))
    valorantextras.bind('<Button-1>', lambda v: openvalorantextrasmenu())

    othermenu = Label(menubar, text="Other", bg="MediumOrchid4", fg="white")
    othermenu.pack(side=LEFT, padx=(0,20))
    othermenu.bind('<Button-1>', lambda o: openothermenumenu())


namebox = Text(root, height=2, width=25, bg=rgb_hack((100, 100, 100)), fg="white")
namebox.place(y=100,x=100)
nameboxtitle = Label(root, text="Name", font=("helvetica",10), bg=rgb_hack((41, 41, 41)), fg="white")
nameboxtitle.place(y=70,x=175)


tagbox = Text(root, height=2, width=10, bg=rgb_hack((100, 100, 100)), fg="white")
tagbox.place(y=100,x=350)
tagboxtitle = Label(root, text="Tag", font=("helvetica", 10), bg=rgb_hack((41, 41, 41)), fg="white")
tagboxtitle.place(y=70,x=375)


hastag = Label(root, text="#", font=("helvetica", 14), fg=rgb_hack((186, 186, 186)), bg=rgb_hack((41, 41, 41)))
hastag.place(y=105,x=318)


searchforplayerbutton = Button(root, text="Search And View Player Stats", height=1, width=25, bg=rgb_hack((100, 100, 100)), fg="white", command=lambda: searchandopen())
searchforplayerbutton.place(y=200,x=175)



title_bar = Frame(root, bg=rgb_hack((80, 80, 80)), relief="raised", bd=0)
title_bar.pack(expand=1, fill=X, anchor="nw")
title_bar.bind('<B1-Motion>', move)


title_bar_title = Label(title_bar, text="Valorant Stat Tracker", bg=rgb_hack((80,80,80)),bd=0,fg='white',font=("helvetica", 10),highlightthickness=0)
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

valorantextras = Label(menubar, text="Valorant Extras", bg="MediumOrchid4", fg="white")
valorantextras.pack(side=LEFT, padx=(0,20))
valorantextras.bind('<Button-1>', lambda v: openvalorantextrasmenu())

othermenu = Label(menubar, text="Other", bg="MediumOrchid4", fg="white")
othermenu.pack(side=LEFT, padx=(0,20))
othermenu.bind('<Button-1>', lambda o: openothermenumenu())



root.bind('<Control-a>', lambda a:agents())
root.bind('<Control-w>', lambda w:weapons())
root.bind('<Control-m>', lambda m:maps())
root.bind('<Control-c>', lambda c:cards())
root.bind('<Control-b>', lambda b:buddies())
root.bind('<Control-s>', lambda s:sprays())
root.bind('<Return>', lambda r: searchandopen())
root.bind('<Escape>', lambda q: root.destroy())



root.mainloop()