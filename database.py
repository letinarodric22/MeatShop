import psycopg2
# psycopg2 is a popular Python adapter for PostgreSQL that allows you to interact with PostgreSQL databases using Python code

try:
    conn = psycopg2.connect("dbname= esipil user=postgres password=1234")
    cur =conn.cursor()
except Exception as e:
    print(e)

def fetch_data(tbname):
    try:
        q = "SELECT * FROM " + tbname + ";"
        cur.execute(q)
        records = cur.fetchall()
        return records 
    except Exception as e:
        return e   
    
def insert_user(v):
    vs = str(v)
    q = "insert into users(full_name,email,user_type, user_status, password, created_at, dob) "\
        "values" + vs
    cur.execute(q)
    conn.commit()
    return q