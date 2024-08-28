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
            log_action("Create Table", f"Table '{table_name}' created with columns {columns}")
        except Exception as e:
            message = str(e)
            log_action("Create Table Error", f"Error: {message}")
        finally:
            conn.close()
    else:
        message = "Database connection failed."
        log_action("Create Table Error", message)
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
            log_action("Delete Table", f"Table '{table_name}' deleted.")
        except Exception as e:
            message = str(e)
            log_action("Delete Table Error", f"Error: {message}")
        finally:
            conn.close()
    else:
        message = "Database connection failed."
        log_action("Delete Table Error", message)
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
            log_action("Insert Data", f"Data inserted into table '{table_name}' with values {values}.")
        except Exception as e:
            message = str(e)
            log_action("Insert Data Error", f"Error: {message}")
        finally:
            conn.close()
    else:
        message = "Database connection failed."
        log_action("Insert Data Error", message)
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
            log_action("Delete Data", f"Data deleted from table '{table_name}' where {where_clause} with params {params}.")
        except Exception as e:
            message = str(e)
            log_action("Delete Data Error", f"Error: {message}")
        finally:
            conn.close()
    else:
        message = "Database connection failed."
        log_action("Delete Data Error", message)
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
            log_action("Update Data", f"Data updated in table '{table_name}' with set clause '{set_clause}' where {where_clause} with params {params}.")
        except Exception as e:
            message = str(e)
            log_action("Update Data Error", f"Error: {message}")
        finally:
            conn.close()
    else:
        message = "Database connection failed."
        log_action("Update Data Error", message)
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
            log_action("Query Data", f"Queried data from table '{table_name}'.")
        except Exception as e:
            result = {"error": str(e)}
            log_action("Query Data Error", f"Error: {result['error']}")
        finally:
            conn.close()
    else:
        result = {"error": "Database connection failed."}
        log_action("Query Data Error", result["error"])
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
            log_action("Display Schema", f"Displayed schema for table '{table_name}'.")
        except Exception as e:
            result = {"error": str(e)}
            log_action("Display Schema Error", f"Error: {result['error']}")
        finally:
            conn.close()
    else:
        result = {"error": "Database connection failed."}
        log_action("Display Schema Error", result["error"])
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
            log_action("Custom Query", f"Performed custom query on table '{table_name}' with columns '{select_columns}' and where clause '{where_clause}'.")
        except Exception as e:
            result = {"error": str(e)}
            log_action("Custom Query Error", f"Error: {result['error']}")
        finally:
            conn.close()
    else:
        result = {"error": "Database connection failed."}
        log_action("Custom Query Error", result["error"])
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
            log_action("Export CSV", f"Data exported from table '{table_name}' to file '{file_name}'.")
        except Exception as e:
            message = str(e)
            log_action("Export CSV Error", f"Error: {message}")
        finally:
            conn.close()
    else:
        message = "Database connection failed."
        log_action("Export CSV Error", message)
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
            log_action("Import CSV", f"Data imported into table '{table_name}' from file '{file_name}'.")
        except Exception as e:
            message = str(e)
            log_action("Import CSV Error", f"Error: {message}")
        finally:
            conn.close()
    else:
        message = "Database connection failed."
        log_action("Import CSV Error", message)
    return jsonify({"message": message})
  
