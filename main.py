
import pandas as pd
import sqlite3


def read_sql(id_user):
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT * FROM conta_task
                where done = 'Pagar' and user_id = {id_user};
	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db

def read_sql2(id_user):
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT * FROM conta_task
                where done = 'Pago' and user_id = {id_user};
	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db

def read_sql_user(user):
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT id FROM auth_user
                where username = '{user}';
    """

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db


def read_sql_xx():
	conn = sqlite3.connect('db.sqlite3')
	sql_datas = f"""
				SELECT id FROM auth_user;

	"""

	read_db = pd.read_sql_query(sql_datas, conn)
	conn.close()
	
	return read_db