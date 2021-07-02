from tdsecrets import TDUser
import tkinter as tk
import tkinter.simpledialog as sd
import tkinter.messagebox as mb



class TDGuiSession:
    secret_user: TDUser

    def __init__(self):
        super().__init__()

session_ = TDGuiSession()
window = tk.Tk()
welcome_lbl = tk.Label(text="Willkommen bei TD Secrets, deinem Passwortmanager")
welcome_lbl.pack()
state_lbl = tk.Label(text="Du bist nicht verbunden, nutze LogIn")
state_lbl.pack()
def login():
    usrbase = sd.askstring("Input", "Was ist der Datenbankname?", parent=window)
    seeds = []
    for i in range(4):
        seedi = sd.askstring("Input", f"Gebe Seed {i+1} ein", parent=window)
        seeds.append(seedi)
    session_.secret_user = TDUser(usrbase, seeds)
    print(session_.secret_user.base_secrets)
    state_lbl["text"] = f"Du bist mit {usrbase} verbunden"
login_btn = tk.Button(text="LogIn", command=login)
login_btn.pack()
def newpw():
    desc = sd.askstring("Input", "Für was ist das Passwort?", parent=window)
    usr = sd.askstring("Input", "Was ist der Username?", parent=window)
    pwd = sd.askstring("Input", "Was ist das Passwort?", parent=window)
    session_.secret_user.put(desc, usr, pwd)
new_btn = tk.Button(text="Neues Passwort", command=newpw)
new_btn.pack()
def getpw():
    desc = sd.askstring("Input", "Für was ist das Passwort?", parent=window)
    usr, pw, pwid = session_.secret_user.get(description=desc)
    mb.showinfo("Information", f"Dein Passwort für {desc} ist: {usr}: {pw}")
get_btn = tk.Button(text="Zeige Passwort", command=getpw)
get_btn.pack()
def showdecs():
    decs = session_.secret_user.secrets["dsc"]
    decs_ = "Deine Beschreibungen:\n"
    for dsc in decs:
        decs_ += f"{dsc}\n"
    mb.showinfo("Information", decs_)
show_btn = tk.Button(text="Zeige alle Beschreibungen", command=showdecs)
show_btn.pack()


window.mainloop()



