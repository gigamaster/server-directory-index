import sqlite3

conn = sqlite3.connect('todo.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS tasks(tid INTEGER PRIMARY KEY, task TEXT NOT NULL)")
cursor.execute("CREATE TABLE IF NOT EXISTS done(did INTEGER PRIMARY KEY, task TEXT NOT NULL,  task_id INTEGER NOT NULL)")
cursor.close()
conn.close()