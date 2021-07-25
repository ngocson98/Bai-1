from database import cursor, db

def add_log(text, user):
    sql = ("INSERT INTO logs(text, user) VALUES ($d, %d)")
    cursor.execute(sql, (text, user,))
    db.commit()
    log_id = cursor.lastrowid
    print("Added log {}".format(log_id))

def get_logs():
    sql = ("SELECT * FORM logs ORDER BY created DESC")
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        print(row)


add_log = ('this is log one', 'Brad')
add_log = ('This is log two', 'Jeff')
add_log = ('This is log three', 'Jane')

get_logs()