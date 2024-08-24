import mysql.connector as c
from mysql.connector import Error

def connect_to_db(host, user, password, database=None):
    """Connect to the MySQL database."""
    try:
        if database:
            conn = c.connect(host=host, user=user, password=password, database=database)
        else:
            conn = c.connect(host=host, user=user, password=password)
        if conn.is_connected():
            print("Connected to MySQL database")
            return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def execute_query(conn, query, params=()):
    """Execute a single SQL query."""
    try:
        mycursor = conn.cursor()
        mycursor.execute(query, params)
        conn.commit()
        return mycursor.fetchall()
    except Error as e:
        print(f"Error executing query: {e}")
        return None

def create_table(conn, table_name, columns):
    """Create a table in the database."""
    columns_definitions = ', '.join([f"{name} {type_}" for name, type_ in columns.items()])
    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_definitions})"
    execute_query(conn, query)

def delete_table(conn, table_name):
    """Delete a table from the database."""
    query = f"DROP TABLE IF EXISTS {table_name}"
    execute_query(conn, query)

def insert_data(conn, table_name, data):
    """Insert data into a table."""
    columns = ', '.join(data.keys())
    placeholders = ', '.join(['%s'] * len(data))
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    execute_query(conn, query, tuple(data.values()))

def delete_data(conn, table_name, where_clause, params):
    """Delete data from a table."""
    query = f"DELETE FROM {table_name} WHERE {where_clause}"
    execute_query(conn, query, params)

def update_data(conn, table_name, set_clause, where_clause, params):
    """Update data in a table."""
    query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
    execute_query(conn, query, params)

def query_data(conn, table_name):
    """Query and display data from a table."""
    query = f"SELECT * FROM {table_name}"
    rows = execute_query(conn, query)
    for row in rows:
        print(row)

def main():
    host = 'localhost'
    user = 'root'
    password = '1234'
    database = 'dsb'

    conn = connect_to_db(host, user, password, database)

    if conn:
        while True:
            print("\nOptions:")
            print("1. Create table")
            print("2. Delete table")
            print("3. Insert data")
            print("4. Delete data")
            print("5. Update data")
            print("6. Query data")
            print("7. Exit")

            choice = input("Enter choice: ").strip()

            if choice == '1':
                table_name = input("Enter table name: ").strip()
                columns = {}
                while True:
                    column_name = input("Enter column name (or type 'done' to finish): ").strip()
                    if column_name.lower() == 'done':
                        break
                    column_type = input("Enter column type (INT, VARCHAR, CHAR): ").strip().upper()
                    if column_type == 'VARCHAR':
                        length = input("Enter length for VARCHAR (e.g., 255): ").strip()
                        columns[column_name] = f"{column_type}({length})"
                    elif column_type in ['INT', 'CHAR']:
                        if column_type == 'CHAR':
                            length = input("Enter length for CHAR (e.g., 10): ").strip()
                            columns[column_name] = f"{column_type}({length})"
                        else:
                            columns[column_name] = column_type
                    else:
                        print("Invalid type. Please enter INT, VARCHAR, or CHAR.")
                create_table(conn, table_name, columns)
                print("Table created successfully.")

            elif choice == '2':
                table_name = input("Enter table name to delete: ").strip()
                delete_table(conn, table_name)
                print("Table deleted successfully.")

            elif choice == '3':
                table_name = input("Enter table name: ").strip()
                data = {}
                while True:
                    column_name = input("Enter column name (or type 'done' to finish): ").strip()
                    if column_name.lower() == 'done':
                        break
                    value = input(f"Enter value for {column_name}: ").strip()
                    data[column_name] = value
                insert_data(conn, table_name, data)
                print("Data inserted successfully.")

            elif choice == '4':
                table_name = input("Enter table name: ").strip()
                where_clause = input("Enter where clause (e.g., id = %s): ").strip()
                params = input("Enter parameters for where clause, separated by commas: ").strip().split(',')
                delete_data(conn, table_name, where_clause, params)
                print("Data deleted successfully.")

            elif choice == '5':
                table_name = input("Enter table name: ").strip()
                set_clause = input("Enter set clause (e.g., name = %s, age = %s): ").strip()
                where_clause = input("Enter where clause (e.g., id = %s): ").strip()
                params = input("Enter parameters for set clause and where clause, separated by commas: ").strip().split(',')
                update_data(conn, table_name, set_clause, where_clause, params)
                print("Data updated successfully.")

            elif choice == '6':
                table_name = input("Enter table name: ").strip()
                query_data(conn, table_name)

            elif choice == '7':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")

        conn.close()

if __name__ == "__main__":
    main()
