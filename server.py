import MySQLdb

database_connectie = MySQLdb.connect(host="localhost",user="root",passwd="//,db="chat")

cur = database_connectie.cursor()


def welkom():
    welkom_input = input("Welkom type 1 om te registreren en 2 om in teloggen ")
    if welkom_input == "1":
        registreren()
    elif welkom_input == "2":
        inlogen()
