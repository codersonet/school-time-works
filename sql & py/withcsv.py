import mysql.connector as c
from mysql.connector import Error
import csv

def connect_to_db(host, user, password, database=None):
    try:
        conn = c.connect(host=host, user=user, password=password, database=database)
        if conn.is_connected():
            print("Connected to MySQL database")
            return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    return None

def execute_query(conn, query, params=()):
    try:
        mycursor = conn.cursor()
        mycursor.execute(query, params)
        conn.commit()
        return mycursor.fetchall()
    except Error as e:
        print(f"Error executing query: {e}")
        return None

def table_exists(conn, table_name):
    query = "SHOW TABLES LIKE %s"
    result = execute_query(conn, query, (table_name,))
    return bool(result)

def column_exists(conn, table_name, column_name):
    query = f"SHOW COLUMNS FROM {table_name} LIKE %s"
    result = execute_query(conn, query, (column_name,))
    return bool(result)

def create_table(conn, table_name, columns):
    if table_exists(conn, table_name):
        print(f"Table '{table_name}' already exists.")
        return
    columns_definitions = ', '.join([f"{name} {type_}" for name, type_ in columns.items()])
    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_definitions})"
    execute_query(conn, query)
    print(f"Table '{table_name}' created successfully.")

def delete_table(conn, table_name):
    if not table_exists(conn, table_name):
        print(f"Table '{table_name}' does not exist.")
        return
    query = f"DROP TABLE IF EXISTS {table_name}"
    execute_query(conn, query)
    print(f"Table '{table_name}' deleted successfully.")

def insert_data(conn, table_name, data):
    if not table_exists(conn, table_name):
        print(f"Table '{table_name}' does not exist.")
        return
    columns_query = f"SHOW COLUMNS FROM {table_name}"
    columns = execute_query(conn, columns_query)
    if len(data) != len(columns):
        print(f"Error: Expected {len(columns)} values, but got {len(data)}.")
        return
    columns_names = ', '.join([col[0] for col in columns])
    placeholders = ', '.join(['%s'] * len(data))
    query = f"INSERT INTO {table_name} ({columns_names}) VALUES ({placeholders})"
    execute_query(conn, query, tuple(data))
    print("Data inserted successfully.")

def delete_data(conn, table_name, where_clause, params):
    if not table_exists(conn, table_name):
        print(f"Table '{table_name}' does not exist.")
        return
    query = f"DELETE FROM {table_name} WHERE {where_clause}"
    execute_query(conn, query, params)
    print("Data deleted successfully.")

def update_data(conn, table_name, set_clause, where_clause, params):
    if not table_exists(conn, table_name):
        print(f"Table '{table_name}' does not exist.")
        return
    query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
    execute_query(conn, query, params)
    print("Data updated successfully.")

def query_data(conn, table_name):
    if not table_exists(conn, table_name):
        print(f"Table '{table_name}' does not exist.")
        return
    query = f"SELECT * FROM {table_name}"
    rows = execute_query(conn, query)
    for row in rows:
        print(row)

def display_table_schema(conn, table_name):
    if not table_exists(conn, table_name):
        print(f"Table '{table_name}' does not exist.")
        return
    query = f"DESCRIBE {table_name}"
    rows = execute_query(conn, query)
    print(f"\nSchema of table '{table_name}':")
    for row in rows:
        print(row)

def custom_query(conn, table_name, select_columns, where_clause=None):
    if not table_exists(conn, table_name):
        print(f"Table '{table_name}' does not exist.")
        return
    select_columns = ', '.join(select_columns)
    query = f"SELECT {select_columns} FROM {table_name}"
    if where_clause:
        query += f" WHERE {where_clause}"
    rows = execute_query(conn, query)
    for row in rows:
        print(row)

def export_to_csv(conn, table_name, file_name):
    if not table_exists(conn, table_name):
        print(f"Table '{table_name}' does not exist.")
        return
    query = f"SELECT * FROM {table_name}"
    rows = execute_query(conn, query)
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([i[0] for i in conn.cursor().description])  # Column headers
        writer.writerows(rows)
    print(f"Data exported to {file_name} successfully.")

def import_from_csv(conn, table_name, file_name):
    if not table_exists(conn, table_name):
        print(f"Table '{table_name}' does not exist.")
        return
    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        columns = next(reader)
        query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s'] * len(columns))})"
        for data in reader:
            execute_query(conn, query, tuple(data))
    print(f"Data imported from {file_name} successfully.")

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
            print("7. Display table schema")
            print("8. Custom query")
            print("9. Export to CSV")
            print("10. Import from CSV")
            print("11. Exit")

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

            elif choice == '2':
                table_name = input("Enter table name to delete: ").strip()
                delete_table(conn, table_name)

            elif choice == '3':
                table_name = input("Enter table name: ").strip()
                columns_query = f"SHOW COLUMNS FROM {table_name}"
                columns = execute_query(conn, columns_query)
                if columns is None or len(columns) == 0:
                    print(f"Table '{table_name}' does not exist or has no columns.")
                    continue
                data = []
                for col in columns:
                    value = input(f"Enter value for {col[0]} ({col[1]}): ").strip()
                    data.append(value)
                insert_data(conn, table_name, data)

            elif choice == '4':
                table_name = input("Enter table name: ").strip()
                where_clause = input("Enter where clause (e.g., id = %s): ").strip()
                params = input("Enter parameters for where clause, separated by commas: ").strip().split(',')
                delete_data(conn, table_name, where_clause, params)

            elif choice == '5':
                table_name = input("Enter table name: ").strip()
                set_clause = input("Enter set clause (e.g., name = %s, age = %s): ").strip()
                where_clause = input("Enter where clause (e.g., id = %s): ").strip()
                params = input("Enter parameters for set clause and where clause, separated by commas: ").strip().split(',')
                update_data(conn, table_name, set_clause, where_clause, params)

            elif choice == '6':
                table_name = input("Enter table name: ").strip()
                query_data(conn, table_name)

            elif choice == '7':
                table_name = input("Enter table name: ").strip()
                display_table_schema(conn, table_name)

            elif choice == '8':
                table_name = input("Enter table name: ").
                select_columns = input("Enter columns to select (comma-separated, or * for all): ").strip().split(',')
                where_clause = input("Enter WHERE clause (optional): ").strip()
                custom_query(conn, table_name, select_columns, where_clause)

            elif choice == '9':
                table_name = input("Enter table name: ").strip()
                file_name = input("Enter CSV file name to export to: ").strip()
                export_to_csv(conn, table_name, file_name)

            elif choice == '10':
                table_name = input("Enter table name: ").strip()
                file_name = input("Enter CSV file name to import from: ").strip()
                import_from_csv(conn, table_name, file_name)

            elif choice == '11':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")

        conn.close()

if __name__ == "__main__":
    main()
