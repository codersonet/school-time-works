# db_manager.py

import mysql.connector as c
from mysql.connector import Error
from .config import config
import csv

def connect_to_db("""host=config.HOST, user=config.USER, password=config.PASSWORD, database=None"""):
    """Connect to the MySQL database."""
    try:
        conn = c.connect(host=config.HOST, user=config.USER, password=config.PASSWORD, database=config.DATABASE)
        if conn.is_connected():
            print("Connected to MySQL database")
            return conn
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    return None

def execute_query(conn, query, params=()):
    """Execute a single SQL query."""
    try:
        cursor = conn.cursor()
        cursor.execute(query, params)
        conn.commit()
        return cursor.fetchall()
    except Error as e:
        print(f"Error executing query: {e}")
        return None

def table_exists(conn, table_name):
    """Check if a table exists in the database."""
    query = "SHOW TABLES LIKE %s"
    result = execute_query(conn, query, (table_name,))
    return bool(result)

def column_exists(conn, table_name, column_name):
    """Check if a column exists in a table."""
    query = f"SHOW COLUMNS FROM {table_name} LIKE %s"
    result = execute_query(conn, query, (column_name,))
    return bool(result)

def create_table(conn, table_name, columns):
    """Create a table in the database."""
    if table_exists(conn, table_name):
        print(f"Table '{table_name}' already exists.")
        return
    columns_definitions = ', '.join([f"{name} {type_}" for name, type_ in columns.items()])
    query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_definitions})"
    execute_query(conn, query)
    print(f"Table '{table_name}' created successfully.")

def delete_table(conn, table_name):
    """Delete a table from the database."""
    if not table_exists(conn, table_name):
        print(f"Table '{table_name}' does not exist.")
        return
    query = f"DROP TABLE IF EXISTS {table_name}"
    execute_query(conn, query)
    print(f"Table '{table_name}' deleted successfully.")

def insert_data(conn, table_name, data):
    """Insert data into a table."""
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
    """Delete data from a table."""
    if not table_exists(conn, table_name):
        print(f"Table '{table_name}' does not exist.")
        return
    query = f"DELETE FROM {table_name} WHERE {where_clause}"
    execute_query(conn, query, params)
    print("Data deleted successfully.")

def update_data(conn, table_name, set_clause, where_clause, params):
    """Update data in a table."""
    if not table_exists(conn, table_name):
        print(f"Table '{table_name}' does not exist.")
        return
    query = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
    execute_query(conn, query, params)
    print("Data updated successfully.")

def query_data(conn, table_name):
    """Query and display data from a table."""
    if not table_exists(conn, table_name):
        print(f"Table '{table_name}' does not exist.")
        return
    query = f"SELECT * FROM {table_name}"
    rows = execute_query(conn, query)
    for row in rows:
        print(row)

def display_table_schema(conn, table_name):
    """Display the schema of a table."""
    if not table_exists(conn, table_name):
        print(f"Table '{table_name}' does not exist.")
        return
    query = f"DESCRIBE {table_name}"
    rows = execute_query(conn, query)
    print(f"\nSchema of table '{table_name}':")
    for row in rows:
        print(row)

def custom_query(conn, table_name, select_columns, where_clause=None):
    """Perform a custom query on a table."""
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
    """Export table data to a CSV file."""
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
    """Import data from a CSV file into a table."""
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
  
