import frappe

def add_custom_fields():
    if not frappe.db.exists("Custom Field", {"dt": "Customer", "fieldname": "customer_group_count"}):

        frappe.get_doc({
            "doctype": "Custom Field",
            "dt": "Customer",
            "fieldname": "customer_group_count",
            "label": "Customer Group Count",
            "fieldtype": "Int",
            "insert_after": "customer_group",  
            "read_only": 1 
        }).insert()
add_custom_fields()
