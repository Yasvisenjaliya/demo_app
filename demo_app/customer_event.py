# Import the frappe module
import frappe
from frappe.model.document import Document

# Override the on_update method of Customer
@frappe.whitelist()
def override_customer_on_update(self, method):
    if self.primary_address:
        # Display popup message when primary address is selected
        frappe.msgprint(("Customer details updated successfully when primary address is selected."))
