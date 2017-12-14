import MySQLdb
import time


database_connectie = MySQLdb.connect(host="localhost",user="root",passwd="/0",db="chat")

cur = database_connectie.cursor()


def ruimten(hoeveel):
    for i in range(hoeveel):
        print("")



def inlogen():
    global naam
    global wachtwoord
    print("je bent bij het menu inloggen ")
    naam = input("Type je username ")
    ruimten(3)
    wachtwoord = input("Type je wachtwoord ")
    #Check als het in de databsae id ....
    cur.execute("SELECT * FROM gegevens WHERE naam = %s and wachtwoord = %s", (naam,wachtwoord))
    row = cur.fetchone()
    if row is not None:
        print("Dit account bestaat ")
        chatten()
    if row is None:
        print("Dit account bestaat niet probeer het nog een keer ....  ")
        inlogen()


def chatten():
    print("Welkom bij het chatten... ")
    chat_bericht = input("Type een bericht ")
    cur.execute("INSERT INTO chatbericht (bericht) VALUES (%s)", [chat_bericht])
    database_connectie.commit()
    cur.execute("SELECT bericht FROM chatbericht")
    data = cur.fetchall()
    for row in data :
        print ("user: " + naam + row[0])












def registreren():
    print("je bent nu aan het registreren ")
    naam_maken = input("Type een gebruikersnaam... ")
    wachtwoord_maken = input("Type je wachtwoord... ")
    wachtwoord_maken = input("Herhaal je wachtwoord correct... ")
    cur.execute("INSERT INTO gegevens (naam,wachtwoord) VALUES (%s,%s)", (naam_maken,wachtwoord_maken))
    database_connectie.commit()
    print("De account is succesvol gemaakt u kan nu ermee inloggen ")
    chat_object.welkom()





class chat:
    def welkom(self):
        global welkom_input
        welkom_input = input("Welkom type 1 om inteloggen en 2 om te registreren ")
        if welkom_input == "1":
            inlogen()
        elif welkom_input == "2":
            registreren()
        return welkom_input




#Definieren
chat_object = chat()

welkom_scherm = chat_object.welkom()


#sluiten
cur.close ()
database_connectie.close ()
