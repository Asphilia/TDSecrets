#this is a secret library to make passwords secret and find he right password
import random
import pandas as pd
import os.path

class TDSecret:
    def __init__(self, seeds):
        super().__init__()
        self.td_dict =  {2: ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "ä", "ö", "ü"],
        1: ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Ä", "Ö", "Ü"],
        3: [".", ":", ",", ";", "#", "+", "*", "~", "-", "_", "?", "ß", "=", ")", "(", "/", "&", "%", "$", "§", "!", "@", "}", "]", "[", "{", "€", "\"", "<", ">", "|"],
        4: ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]}
        self.shuffle(seeds)

    def krypta1(self, wort):
        result = []
        for c in wort:
            if c in self.td_dict[1]:
                index = self.td_dict[1].index(c)
                result.append(int(f"1{index}"))
            elif c in self.td_dict[2]:
                index = self.td_dict[2].index(c)
                result.append(int(f"2{index}"))
            elif c in self.td_dict[3]:
                index = self.td_dict[3].index(c)
                result.append(int(f"3{index}"))
            elif c in self.td_dict[4]:
                index = self.td_dict[4].index(c)
                result.append(int(f"4{index}"))
            else:
                print(f"character {c} not a possible input!")
                return []
        return result

    def krypta2(self, wort):
        result = ""
        for c in wort:
            wort_ = str(c)
            a = wort_[0]
            b = wort_[1:]
            r = self.td_dict[int(a)][int(b)]
            result += r
        return result

    def shuffle(self, seeds):
        for i in range(4):
            random.Random(seeds[i]).shuffle(self.td_dict[i+1])

    def encrypt(self, word):
        return self.krypta1(word)

    def decrypt(self, word):
        return self.krypta2(word)

class TDUser:
    def __init__(self, userbasename, seeds):
        super().__init__()
        self.base_secrets = userbasename + ".txt"
        if os.path.exists(self.base_secrets):
            self.secrets = pd.read_csv(self.base_secrets, names=["dsc", "usr", "pwd"])
        else:
            self.secrets = pd.DataFrame(columns= ["dsc", "usr", "pwd"])
        self.cryptograph = TDSecret(seeds)

    def save(self):
        self.secrets.to_csv(self.base_secrets, header=False)

    def get(self, pw_id=-1, description=None):
        if (pw_id == -1) and (not description):
            print("You must set id or description!")
            return None
        if description:
            pw_id = self.find(description)
        plain_secret = self.secrets["pwd"][pw_id].split(" ")
        the_secret = [int(i) for i in plain_secret[:-1]]
        return self.secrets["usr"][pw_id], self.cryptograph.decrypt(the_secret), pw_id

    def put(self, description, usrname, secret):
        secret_ = self.cryptograph.encrypt(secret)
        secreta_ = ""
        for si in secret_:
            secreta_ += f"{si} "
        self.secrets = self.secrets.append({"usr": usrname, "pwd": secreta_, "dsc": description}, ignore_index=True)
        self.save()
        return self.secrets.index[-1]

    def change_pw(self, pw_id, secret):
        secret_ = self.cryptograph.encrypt(secret)
        secreta_ = ""
        for si in secret_:
            secreta_ += f"{si} "
        self.secrets["pwd"][pw_id] = secreta_
        self.save()
        return pw_id

    def change_usr(self, pw_id, usrname):
        self.secrets["usr"][pw_id] = usrname
        self.save()
        return pw_id

    def change_description(self, pw_id, description):
        self.secrets["dsc"][pw_id] = description
        self.save()
        return pw_id

    def find(self, description):
        return self.secrets["dsc"][self.secrets["dsc"] == description].index[0]
        