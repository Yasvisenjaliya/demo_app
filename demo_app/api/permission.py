# demo_app/api/permission.py

import frappe

def has_app_permission():
    # Get the current user
    user = frappe.session.user
    
    # Define logic to check if the user has permission to see the app
    if user == "Administrator":
        return True
    return False
