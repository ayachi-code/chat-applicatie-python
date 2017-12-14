import MySQLdb

database_connectie = MySQLdb.connect(host="localhost",user="root",passwd="almujaahid/0",db="chat")

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
    while row is not None:
        print(row)
        row = cur.fetchone()




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
