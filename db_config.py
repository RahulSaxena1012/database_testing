from sqlalchemy import create_engine

def get_db_connection():
    engine = create_engine('mysql+pymysql://root:yourpassword@localhost:3306/testdb')
    connection = engine.connect()
    return connection

# Test the connection
if __name__ == "__main__":
    conn = get_db_connection()
    print("Connection successful!")
    conn.close()
