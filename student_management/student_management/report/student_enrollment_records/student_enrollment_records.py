import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data

def get_columns():
    return [
        {"label": "Course", "fieldname": "course", "fieldtype": "Data", "width": 200},
        {"label": "Status", "fieldname": "status", "fieldtype": "Data", "width": 150},
        {"label": "Enrollment Count", "fieldname": "enrollment_count", "fieldtype": "Int", "width": 150}
    ]

def get_data(filters):
    query = """
        SELECT 
            se.course AS course, 
            se.status, 
            COUNT(se.name) AS enrollment_count
        FROM 
            `tabStudent Enrollment` se
        GROUP BY 
            se.course, se.status
        ORDER BY 
            se.course, se.status
    """
    return frappe.db.sql(query, as_dict=True)
