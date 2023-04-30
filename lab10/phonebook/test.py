import psycopg2
from config import config


def insert_user():
        a = str(input("Enter your nickname: "))
        sql = """SELECT * from users WHERE user_name = '{}' """.format(a)
        
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()

            cur.execute(sql)
            result = cur.fetchone() 
            print(result)

            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()




if __name__ == '__main__':
    insert_user()