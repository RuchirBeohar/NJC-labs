import sqlite3
import traceback
conn=None
try:
    conn=sqlite3.connect("./moviesdata.db")
    print("DB Connected Successfuly :)")
    cur = conn.cursor()
    cur.execute("Select movieName, actor, actress, director, year from moviesData")
    for x in cur.fetchall():
        movieName, actor, actress, director, year = x
        print("movieName: "+ movieName +", Actor: "+actor+ ", Actress: " + actress +", Director: "+director + ", Year: "+str(year))
except sqlite3.DatabaseError:
    print("DB Not Connected :(")
    print("Reason:",traceback.format_exc())
finally:
    if conn is not None:
        conn.close()
        print("DB Disconnected Successfully :)")
