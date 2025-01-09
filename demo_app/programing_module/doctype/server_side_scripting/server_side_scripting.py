# Copyright (c) 2025, dcode and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ServerSideScripting(Document):
	
	def validate(self):
		frappe.msgprint("Hello")
