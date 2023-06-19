import sqlite3
from sqlite3 import Error

def create_connection(db_file):
	conn = None
	try:
		conn = sqlite3.connect(db_file)
	except Error as e:
		print(e)
		
	return conn
	
def create_table(conn):
	sql_projects = """
	CREATE TABLE IF NOT EXISTS led(
	      id INTERGER PRIMARY KEY AUTOINCREMENT,
	      date TEXT NOT NULL,
	      state INTERGER NOT NULL
	);
	"""
	
	try:
		cursor = conn.cursor()
		cursor.execute(sql_projects)
		print("table created successfully")
	except Error as e:
		print(e)
		
def insert_data(state):
	conn = create_connection('iot.db')
	create_table(conn)
	
	sql_insert = """
	INSERT INTO led(date, state)VALUES(datetime('now'), ?);
	"""
		cursor = conn.cursor()
		cursor.execute(sql_insert, (state,))
		conn.commit()
		conn.close()	

