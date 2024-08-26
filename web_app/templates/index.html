# app/routes.py

from flask import Blueprint, request, jsonify
from .db_manager import *

routes = Blueprint('routes', __name__)

# Route to create a table
@routes.route('/create_table', methods=['POST'])
def create_table_route():
    data = request.json
    table_name = data.get('table_name')
    columns = data.get('columns')
    conn = connect_to_db()
    if conn:
        create_table(conn, table_name, columns)
        conn.close()
    return jsonify({"message": f"Table '{table_name}' created successfully."})

# Route to delete a table
@routes.route('/delete_table', methods=['POST'])
def delete_table_route():
    data = request.json
    table_name = data.get('table_name')
    conn = connect_to_db()
    if conn:
        delete_table(conn, table_name)
        conn.close()
    return jsonify({"message": f"Table '{table_name}' deleted successfully."})

# Route to insert data into a table
@routes.route('/insert_data', methods=['POST'])
def insert_data_route():
    data = request.json
    table_name = data.get('table_name')
    values = data.get('values')
    conn = connect_to_db()
    if conn:
        insert_data(conn, table_name, values)
        conn.close()
    return jsonify({"message": "Data inserted successfully."})

# Route to delete data from a table
@routes.route('/delete_data', methods=['POST'])
def delete_data_route():
    data = request.json
    table_name = data.get('table_name')
    where_clause = data.get('where_clause')
    params = data.get('params')
    conn = connect_to_db()
    if conn:
        delete_data(conn, table_name, where_clause, params)
        conn.close()
    return jsonify({"message": "Data deleted successfully."})

# Route to update data in a table
@routes.route('/update_data', methods=['POST'])
def update_data_route():
    data = request.json
    table_name = data.get('table_name')
    set_clause = data.get('set_clause')
    where_clause = data.get('where_clause')
    params = data.get('params')
    conn = connect_to_db()
    if conn:
        update_data(conn, table_name, set_clause, where_clause, params)
        conn.close()
    return jsonify({"message": "Data updated successfully."})

# Route to query data from a table
@routes.route('/query_data', methods=['POST'])
def query_data_route():
    data = request.json
    table_name = data.get('table_name')
    conn = connect_to_db()
    if conn:
        rows = query_data(conn, table_name)
        conn.close()
    return jsonify({"data": rows})

# Route to display table schema
@routes.route('/display_schema', methods=['POST'])
def display_schema_route():
    data = request.json
    table_name = data.get('table_name')
    conn = connect_to_db()
    if conn:
        schema = display_table_schema(conn, table_name)
        conn.close()
    return jsonify({"schema": schema})

# Route for a custom query
@routes.route('/custom_query', methods=['POST'])
def custom_query_route():
    data = request.json
    table_name = data.get('table_name')
    select_columns = data.get('select_columns')
    where_clause = data.get('where_clause')
    conn = connect_to_db()
    if conn:
        rows = custom_query(conn, table_name, select_columns, where_clause)
        conn.close()
    return jsonify({"data": rows})

# Route to export data to CSV
@routes.route('/export_csv', methods=['POST'])
def export_csv_route():
    data = request.json
    table_name = data.get('table_name')
    file_name = data.get('file_name')
    conn = connect_to_db()
    if conn:
        export_to_csv(conn, table_name, file_name)
        conn.close()
    return jsonify({"message": f"Data exported to {file_name} successfully."})

# Route to import data from CSV
@routes.route('/import_csv', methods=['POST'])
def import_csv_route():
    data = request.json
    table_name = data.get('table_name')
    file_name = data.get('file_name')
    conn = connect_to_db()
    if conn:
        import_from_csv(conn, table_name, file_name)
        conn.close()
    return jsonify({"message": f"Data imported from {file_name} successfully."})
    
