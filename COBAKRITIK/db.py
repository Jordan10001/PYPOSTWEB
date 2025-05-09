import psycopg2

DB_HOST = 'localhost'
DB_NAME = 'pythonpost'
DB_USER = 'postgres'
DB_PASS = 'admin'

def get_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        print("[DB]✅ Koneksi database berhasil.")
        return conn
    except psycopg2.Error as e:
        print(f"[DB]❌ Gagal koneksi ke database: {e}")
        return None

def insert_kritik(nama, email, kritik):
    conn = get_connection()
    if conn is None:
        return False
    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO kritik (nama, email, kritik) VALUES (%s, %s, %s)",
            (nama, email, kritik)
        )
        conn.commit()
        cur.close()
        conn.close()
        return True
    except psycopg2.Error as e:
        print(f"[DB INSERT ERROR] {e}")
        return False
