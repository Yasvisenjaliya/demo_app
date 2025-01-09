# Copyright (c) 2025, dcode and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class PrintStudentMarks(Document):
    def before_save(self):
        calculate_marks(self)

def calculate_marks(doc):
    total_marks_obtained = 0
    total_max_marks = 0

    for row in doc.subject_marks:
        try:
            marks_obtained = float(row.marks_obtained) if row.marks_obtained else 0
            max_marks = float(row.max_marks) if row.max_marks else 0

            total_marks_obtained += marks_obtained
            total_max_marks += max_marks
        except ValueError:
            frappe.throw(f"Invalid marks or maximum marks in row: {row.idx}")

    if total_max_marks > 0:
        percentage = (total_marks_obtained / total_max_marks) * 100
    else:
        percentage = 0

    doc.total_marks = total_marks_obtained
    doc.maximum_marks = total_max_marks
    doc.percentage = percentage

@frappe.whitelist()
def on_update(doc_name):
    doc = frappe.get_doc("PrintStudentMarks", doc_name)

    calculate_marks(doc)
    doc.save()
