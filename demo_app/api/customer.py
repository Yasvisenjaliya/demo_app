import frappe
import json

@frappe.whitelist(allow_guest=True)
def get_customers(filters=None):
    try:
        if isinstance(filters, str):
            filters = json.loads(filters) 
        
        customers = frappe.get_all(
            "Customer",
            filters=filters, 
            fields=["name", "customer_name", "customer_group", "customer_type"],
            order_by="customer_name asc"  
        )
        
        if not customers:
            return {"status": "success", "message": "No customers found for the given filters."}
        
        return {"status": "success", "data": customers}

    except Exception as e:
        return {"status": "error", "message": str(e)}
