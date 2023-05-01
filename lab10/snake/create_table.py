#!/usr/bin/python

import psycopg2
from config import config


def create_tables():
    sql = """CREATE TABLE snake_scores (
            user_id SERIAL PRIMARY KEY,
            user_nickname VARCHAR(255) NOT NULL,
            user_score SMALLINT NOT NULL,
            user_level SMALLINT NOT NULL)
        """
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()