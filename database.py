import sys
import mysql.connector as MySQLdb
import os


dbcreditials = {    'host':"192.168.1.236",     # your host, usually localhost
                    'user':"root",          # your username
                    'passwd':"Wenderslover1",      # your password
                    'db':"home" }

def fetchAsDict( sql, param ):
	db = MySQLdb.connect( **dbcreditials )
	error = None
	try:
		#dictCursor = db.cursor(MySQLdb.cursors.DictCursor)
		dictCursor = db.cursor(dictionary=True)
		dictCursor.execute( sql, param )
		resultSet = dictCursor.fetchall()
		dictCursor.close
	except Exception as e:
		error = str(e)

		resultSet = {}
		print ("<---------------- Database error start ---------------------->")
		print (error)
		print ("<----------------- Database error end ----------------------->")
	db.close()
	return ( error, resultSet )


def execute( sql,params ):  
	error = None
	try:
		db = MySQLdb.connect( **dbcreditials  )	    
		cur = db.cursor()    
		cur.execute( sql,params ) 
		db.commit()
	except Exception as e:
		error = str(e)
		print ("<---------------- Database error start ---------------------->")
		print (error)
		print ("<----------------- Database error end ----------------------->")
    
	db.close()
	return error 
