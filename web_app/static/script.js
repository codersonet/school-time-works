// static/script.js

document.addEventListener('DOMContentLoaded', () => {
    // Handle Create Table
    const createTableForm = document.getElementById('createTableForm');
    createTableForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const tableName = document.getElementById('tableName').value;
        const columns = document.getElementById('columns').value;
        const columnsArray = columns.split(',').reduce((acc, col) => {
            const [name, type] = col.split(':');
            acc[name] = type.toUpperCase();
            return acc;
        }, {});

        fetch('/create_table', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                table_name: tableName,
                columns: columnsArray
            })
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    // Handle Delete Table
    const deleteTableForm = document.getElementById('deleteTableForm');
    deleteTableForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const tableName = document.getElementById('deleteTableName').value;

        fetch('/delete_table', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                table_name: tableName
            })
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    // Handle Insert Data
    const insertDataForm = document.getElementById('insertDataForm');
    insertDataForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const tableName = document.getElementById('insertTableName').value;
        const values = document.getElementById('values').value.split(',');

        fetch('/insert_data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                table_name: tableName,
                values: values
            })
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    // Handle Delete Data
    const deleteDataForm = document.getElementById('deleteDataForm');
    deleteDataForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const tableName = document.getElementById('deleteDataTableName').value;
        const whereClause = document.getElementById('whereClause').value;
        const params = document.getElementById('params').value.split(',');

        fetch('/delete_data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                table_name: tableName,
                where_clause: whereClause,
                params: params
            })
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    // Handle Update Data
    const updateDataForm = document.getElementById('updateDataForm');
    updateDataForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const tableName = document.getElementById('updateTableName').value;
        const setClause = document.getElementById('setClause').value;
        const whereClause = document.getElementById('updateWhereClause').value;
        const params = document.getElementById('updateParams').value.split(',');

        fetch('/update_data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                table_name: tableName,
                set_clause: setClause,
                where_clause: whereClause,
                params: params
            })
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    // Handle Query Data
    const queryDataForm = document.getElementById('queryDataForm');
    queryDataForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const tableName = document.getElementById('queryTableName').value;

        fetch('/query_data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                table_name: tableName
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            alert("Data queried successfully. Check console for output.");
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    // Handle Display Table Schema
    const displaySchemaForm = document.getElementById('displaySchemaForm');
    displaySchemaForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const tableName = document.getElementById('schemaTableName').value;

        fetch('/display_schema', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                table_name: tableName
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            alert("Schema displayed successfully. Check console for output.");
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    // Handle Custom Query
    const customQueryForm = document.getElementById('customQueryForm');
    customQueryForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const tableName = document.getElementById('customQueryTableName').value;
        const selectColumns = document.getElementById('selectColumns').value.split(',');
        const whereClause = document.getElementById('customWhereClause').value;

        fetch('/custom_query', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                table_name: tableName,
                select_columns: selectColumns,
                where_clause: whereClause
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            alert("Custom query executed successfully. Check console for output.");
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    // Handle Export to CSV
    const exportCsvForm = document.getElementById('exportCsvForm');
    exportCsvForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const tableName = document.getElementById('exportTableName').value;
        const fileName = document.getElementById('exportFileName').value;

        fetch('/export_csv', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                table_name: tableName,
                file_name: fileName
            })
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });

    // Handle Import from CSV
    const importCsvForm = document.getElementById('importCsvForm');
    importCsvForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const tableName = document.getElementById('importTableName').value;
        const fileName = document.getElementById('importFileName').value;

        fetch('/import_csv', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                table_name: tableName,
                file_name: fileName
            })
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
