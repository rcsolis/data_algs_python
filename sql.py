import sqlite3
con = sqlite3.connect("testdb.db")
try:
    cur = con.cursor()
    # Create table
    cur.execute('''CREATE TABLE IF NOT EXISTS person
               (name text, lastname text, age int, salary real)''')
    # Insert a row of data
    cur.execute("INSERT INTO person VALUES ('Rafael','BUY',35,3500)")
    # Save (commit) the changes
    con.commit()

    res = cur.execute("SELECT * FROM person")
    for row in res:
        print(row)
except (sqlite3.Error, Exception) as e:
    print(e)
# Close connection
finally:
    con.close()
