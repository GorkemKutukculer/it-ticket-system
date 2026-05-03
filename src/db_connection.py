import pyodbc

class DatabaseConnection:
    def __init__(self):
        self.server = 'DESKTOP-0I931R1'
        self.database = 'IT_Support_DB'
        
        self.conn_str = (
            f"Driver={{SQL Server}};"
            f"Server={self.server};"
            f"Database={self.database};"
            f"Trusted_Connection=yes;"
        )

    def connect(self):
        try:
            conn = pyodbc.connect(self.conn_str)
            print("Veritabanı bağlantısı BAŞARILI!")
            return conn
        except Exception as e:
            print(f"Bağlantı hatası oluştu: {e}")
            return None

if __name__ == "__main__":
    db = DatabaseConnection()
    db.connect()