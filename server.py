import MySQLdb

database_connectie = MySQLdb.connect(host="localhost",user="root",passwd="a",db="chat")

cur = database_connectie.cursor()
