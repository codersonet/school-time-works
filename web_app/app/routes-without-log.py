from flask import Blueprint, request, jsonify
from .db_manager import connect_to_db, create_table, delete_table, insert_data, delete_data, update_data, query_data, display_table_schema, custom_query, export_to_csv, import_from_csv
from .logging import log_action

routes = Blueprint('routes', __name__)

# Route to create a table
@routes.route('/create_table', methods=['POST'])
def create_table_route():
    data = request.json
    table_name = data.get('table_name')
    columns = data.get('columns')
    conn = connect_to_db()
    if conn:
        try:
            create_table(conn, table_name, columns)
            message = f"Table '{table_name}' created successfully."
        except Exception as e:
            message = str(e)
        finally:
            conn.close()
    else:
        message = "Database connection failed."
    return jsonify({"message": message})

# Route to delete a table
@routes.route('/delete_table', methods=['POST'])
def delete_table_route():
    data = request.json
    table_name = data.get('table_name')
    conn = connect_to_db()
    if conn:
        try:
            delete_table(conn, table_name)
            message = f"Table '{table_name}' deleted successfully."
        except Exception as e:
            message = str(e)
        finally:
            conn.close()
    else:
        message = "Database connection failed."
    return jsonify({"message": message})

# Route to insert data into a table
@routes.route('/insert_data', methods=['POST'])
def insert_data_route():
    data = request.json
    table_name = data.get('table_name')
    values = data.get('values')
    conn = connect_to_db()
    if conn:
        try:
            insert_data(conn, table_name, values)
            message = "Data inserted successfully."
        except Exception as e:
            message = str(e)
        finally:
            conn.close()
    else:
        message = "Database connection failed."
    return jsonify({"message": message})

# Route to delete data from a table
@routes.route('/delete_data', methods=['POST'])
def delete_data_route():
    data = request.json
    table_name = data.get('table_name')
    where_clause = data.get('where_clause')
    params = data.get('params')
    conn = connect_to_db()
    if conn:
        try:
            delete_data(conn, table_name, where_clause, params)
            message = "Data deleted successfully."
        except Exception as e:
            message = str(e)
        finally:
            conn.close()
    else:
        message = "Database connection failed."
    return jsonify({"message": message})

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
        try:
            update_data(conn, table_name, set_clause, where_clause, params)
            message = "Data updated successfully."
        except Exception as e:
            message = str(e)
        finally:
            conn.close()
    else:
        message = "Database connection failed."
    return jsonify({"message": message})

# Route to query data from a table
@routes.route('/query_data', methods=['POST'])
def query_data_route():
    data = request.json
    table_name = data.get('table_name')
    conn = connect_to_db()
    if conn:
        try:
            rows = query_data(conn, table_name)
            result = {"data": rows}
        except Exception as e:
            result = {"error": str(e)}
        finally:
            conn.close()
    else:
        result = {"error": "Database connection failed."}
    return jsonify(result)

# Route to display table schema
@routes.route('/display_schema', methods=['POST'])
def display_schema_route():
    data = request.json
    table_name = data.get('table_name')
    conn = connect_to_db()
    if conn:
        try:
            schema = display_table_schema(conn, table_name)
            result = {"schema": schema}
        except Exception as e:
            result = {"error": str(e)}
        finally:
            conn.close()
    else:
        result = {"error": "Database connection failed."}
    return jsonify(result)

# Route for a custom query
@routes.route('/custom_query', methods=['POST'])
def custom_query_route():
    data = request.json
    table_name = data.get('table_name')
    select_columns = data.get('select_columns')
    where_clause = data.get('where_clause')
    conn = connect_to_db()
    if conn:
        try:
            rows = custom_query(conn, table_name, select_columns, where_clause)
            result = {"data": rows}
        except Exception as e:
            result = {"error": str(e)}
        finally:
            conn.close()
    else:
        result = {"error": "Database connection failed."}
    return jsonify(result)

# Route to export data to CSV
@routes.route('/export_csv', methods=['POST'])
def export_csv_route():
    data = request.json
    table_name = data.get('table_name')
    file_name = data.get('file_name')
    conn = connect_to_db()
    if conn:
        try:
            export_to_csv(conn, table_name, file_name)
            message = f"Data exported to {file_name} successfully."
        except Exception as e:
            message = str(e)
        finally:
            conn.close()
    else:
        message = "Database connection failed."
    return jsonify({"message": message})

# Route to import data from CSV
@routes.route('/import_csv', methods=['POST'])
def import_csv_route():
    data = request.json
    table_name = data.get('table_name')
    file_name = data.get('file_name')
    conn = connect_to_db()
    if conn:
        try:
            import_from_csv(conn, table_name, file_name)
            message = f"Data imported from {file_name} successfully."
        except Exception as e:
            message = str(e)
        finally:
            conn.close()
    else:
        message = "Database connection failed."
    return jsonify({"message": message})
