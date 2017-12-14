import MySQLdb

database_connectie = MySQLdb.connect(host="localhost",user="root",passwd="test",db="chat")

cur = database_connectie.cursor()


def inlogen():
    print("je bent bij het menu inloggen ")




class chat:
    def welkom(self):
        global welkom_input
        welkom_input = input("Welkom type 1 om te registreren en 2 om in teloggen ")
        if welkom_input == "1":
            inlogen()
        elif welkom_input == "2":
            registreren()
        return welkom_input




#Definieren
chat_object = chat()

welkom_scherm = chat_object.welkom()
