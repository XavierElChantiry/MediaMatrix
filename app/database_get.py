import mysql.connector
from os import environ
from dotenv import load_dotenv

load_dotenv()

def get_titles(title="", row_count=5):
    db_conn = mysql.connector.connect(
        host=environ["MYSQL_HOSTNAME"],
        user=environ["MYSQL_USER"],
        password=environ["MYSQL_PASSWORD"],
        database=environ["MYSQL_DATABASE"],
        port=environ["MYSQL_PORT"]
    )
    db_cursor = db_conn.cursor()
    if title == "":
        db_cursor.execute("""
    SELECT * FROM paths
        """)
    else:
        db_cursor.execute("""
    SELECT * FROM paths WHERE title LIKE %s
        """, ("%" + title + "%", ))
    videos = db_cursor.fetchmany(size=row_count)
    
    db_conn.commit()
    db_conn.close()
    return videos

def get_video(id):
    db_conn = mysql.connector.connect(
        host=environ["MYSQL_HOSTNAME"],
        user=environ["MYSQL_USER"],
        password=environ["MYSQL_PASSWORD"],
        database=environ["MYSQL_DATABASE"],
        port=environ["MYSQL_PORT"]
    )
    db_cursor = db_conn.cursor()
    db_cursor.execute("""
SELECT * FROM paths WHERE id = %s;
    """, (id, ))

    video_info = db_cursor.fetchone()
    db_conn.commit()
    db_conn.close()
    return video_info
    