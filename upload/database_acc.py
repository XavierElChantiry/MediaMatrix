import mysql.connector
from os import environ
from dotenv import load_dotenv

load_dotenv()

def upload_to_db(title, path):
    db_conn = mysql.connector.connect(
        host=environ["MYSQL_HOSTNAME"],
        user=environ["MYSQL_USER"],
        password=environ["MYSQL_PASSWORD"],
        database=environ["MYSQL_DATABASE"],
        port=environ["MYSQL_PORT"]
    )
    db_cursor = db_conn.cursor()
    db_cursor.execute("""
    INSERT INTO paths(title, path) VALUES (%s, %s);
    """, (title, path,))
    db_cursor.execute("""
    SELECT LAST_INSERT_ID();
    """)

    video_id = db_cursor.fetchone()
    
    db_conn.commit()
    db_conn.close()
    return f"{video_id[0]}. {title}"