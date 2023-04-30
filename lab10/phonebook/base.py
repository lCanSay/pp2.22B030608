import psycopg2
from config import config


def insert_user():
    a = str(input('Manually or from csv? '))
    if a == "manually":
        sql = """INSERT INTO users(user_name, user_number, user_country)
                VALUES(%s, %s, %s) 
                RETURNING user_id;"""
        conn = None
        user_id = None
        name = str(input("Enter user's name: "))
        number = str(input("Enter user's number: "))
        country = str(input("Enter user's country: "))
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()

            values_insert = (name, number, country)   #parameters for submittion
            cur.execute(sql, values_insert)

            # get the generated id back
            user_id = cur.fetchone()[0]
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()

        return user_id
    else:
        a = str(input("Enter a path to a csv file: "))
        b = ''
        for i in a:
            if a != "\\":
                b = b + i
            else:
                b = b + "\\" + i

        sql = '''COPY users(user_name, user_number, user_country)
                FROM '{}'
                DELIMITER ';'
                ;'''.format(b)
        conn = None
        try:
            params = config()
            conn = psycopg2.connect(**params)
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            cur.close()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
        finally:
            if conn is not None:
                conn.close()


def update_user():
    u_id = str(input("Enter the id: "))
    a = str(input("What do you want to update: "))
    if(a == "name"):
        sql = """ UPDATE users
                    SET user_name = %s
                    WHERE user_id = %s"""
        changable = str(input("Enter new name: "))
    elif(a == "number"):
        sql = """ UPDATE users
                    SET user_number = %s
                    WHERE user_id = %s"""
        changable = str(input("Enter new number: "))
    elif(a == "country"):
        sql = """ UPDATE users
                    SET user_country = %s
                    WHERE user_id = %s"""
        changable = str(input("Enter new country: "))

    
    conn = None
    updated_rows = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (changable, u_id))
        # get the number of updated rows
        updated_rows = cur.rowcount
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return updated_rows

def delete_user():
    a = str(input("By name or by number: "))
    
    if(a == "name"):
        changable = str(input("Enter the name: "))
        sql = """ DELETE FROM users
                    WHERE user_name = %s"""
    elif(a == "number"):
        changable = str(input("Enter the number: "))
        sql = """ DELETE FROM users
                    WHERE user_number = %s"""
    
    conn = None
    updated_rows = 0
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (changable,))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



if __name__ == '__main__':
    delete_user()
