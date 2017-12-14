import MySQLdb

database_connectie = MySQLdb.connect(host="localhost",user="root",passwd="g",db="chat")

cur = database_connectie.cursor()

global welkom_input


class chat:
    def welkom(self):
        welkom_input = input("Welkom type 1 om te registreren en 2 om in teloggen ")
        if welkom_input == "1":
            registreren()
        elif welkom_input == "2":
            inlogen()






#Definieren
chat_object = chat()
