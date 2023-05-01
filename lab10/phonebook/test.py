import psycopg2
from config import config


def fetch_user(user_name):
        sql = """SELECT * from users WHERE user_name = '{}' """.format(user_name)
        
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()

            cur.execute(sql)
            result = cur.fetchone() 

            conn.commit()
            cur.close()
            return result
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close() 



a = str(input("Enter your name: "))
b = fetch_user(a)
print(b)