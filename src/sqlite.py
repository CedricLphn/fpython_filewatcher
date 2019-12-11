import sqlite3


sql = sqlite3.connect("watcher.sqlite")
cursor = sql.cursor()

def init():
    return cursor.execute("CREATE TABLE IF NOT EXISTS directory(filename text, directory text, signature text)")

def write(filename, directory, signature):
    cursor.execute("INSERT INTO directory(filename,directory,signature) VALUES(?,?,?)", [filename, directory, signature])
    sql.commit()

def select(filename):
    cursor.execute("SELECT * FROM directory WHERE filename = ?", [filename])
    return cursor.fetchone()

def select_filename():
    table = []
    cursor.execute("SELECT filename FROM directory")
    data = cursor.fetchall()
    for i in range(0, len(data)):
        table.append(data[i][0])
    return table

def count(filename):
    cursor.execute("SELECT * FROM directory WHERE filename = ?", [filename])
    return len(cursor.fetchall())

def update_signature(filename, signature):
    try:
        cursor.execute("UPDATE directory SET signature = ? WHERE filename=?", [signature, filename])
        sql.commit()
        return True
    except:
        return False
