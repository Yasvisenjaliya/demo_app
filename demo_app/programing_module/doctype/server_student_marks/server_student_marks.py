# Copyright (c) 2025, dcode and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class ServerStudentMarks(Document):
    def before_save(self):
        calculate_marks(self)

def calculate_marks(doc):
    total_marks_obtained = 0
    total_max_marks = 0

    for row in doc.marks_table:
        total_marks_obtained += row.marks
        total_max_marks += row.maximum_marks

    if total_max_marks > 0:
        percentage = (total_marks_obtained / total_max_marks) * 100
    else:
        percentage = 0

    doc.total_marks = total_marks_obtained
    doc.maximum_marks = total_max_marks
    doc.percentage = percentage

# @frappe.whitelist()
# def on_update(self):
# calculate_marks(self)
