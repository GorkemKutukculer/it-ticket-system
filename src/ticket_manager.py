from db_connection import DatabaseConnection

class TicketManager:
    def __init__(self):
        self.db = DatabaseConnection()

    def add_user(self, full_name, email, role='User'):
        conn = self.db.connect()
        if conn:
            cursor = conn.cursor()
            query = "INSERT INTO Users (FullName, Email, Role) VALUES (?, ?, ?)"
            try:
                cursor.execute(query, (full_name, email, role))
                conn.commit()
            except Exception:
                pass
            conn.close()

    def create_ticket(self, title, description, priority, created_by_id):
        conn = self.db.connect()
        if conn:
            cursor = conn.cursor()
            query = "INSERT INTO Tickets (Title, Description, Priority, CreatedBy) VALUES (?, ?, ?, ?)"
            cursor.execute(query, (title, description, priority, created_by_id))
            conn.commit()
            conn.close()

    def get_all_tickets(self):
        conn = self.db.connect()
        if conn:
            cursor = conn.cursor()
            query = """
                SELECT T.TicketID, T.Title, T.Description, T.Priority, T.Status, U.FullName 
                FROM Tickets T
                JOIN Users U ON T.CreatedBy = U.UserID
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            conn.close()
            return rows
        return []

    def get_all_users(self):
        conn = self.db.connect()
        if conn:
            cursor = conn.cursor()
            query = "SELECT UserID, FullName FROM Users"
            cursor.execute(query)
            rows = cursor.fetchall()
            conn.close()
            return rows
        return []

    def update_ticket_status(self, ticket_id, new_status):
        conn = self.db.connect()
        if conn:
            cursor = conn.cursor()
            query = "UPDATE Tickets SET Status = ? WHERE TicketID = ?"
            cursor.execute(query, (new_status, ticket_id))
            if new_status == 'Resolved':
                time_query = "UPDATE Tickets SET ResolvedAt = GETDATE() WHERE TicketID = ?"
                cursor.execute(time_query, (ticket_id,))
            conn.commit()
            conn.close()