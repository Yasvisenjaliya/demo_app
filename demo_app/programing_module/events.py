import frappe
from frappe import _

def validate_student(doc, method):
    if not doc.student_marks:
        frappe.throw(_("No marks found in the student_marks child table."))

    total_marks = 0
    max_marks = 0


    for row in doc.student_marks:
        total_marks += float(row.total_marks)  
        max_marks += float(row.max_marks)  

    # if max_marks == 0:
    #     frappe.throw(_("Max marks cannot be zero."))

    percentage = (total_marks / max_marks) * 100
    doc.percentage = percentage  

    if percentage < 33:
        doc.status = "Failed"
    elif 33 <= percentage <= 50:
        doc.status = "Pass"
    else:
        doc.status = "Excellent"

    print(f"\n\n\n Total Marks: {total_marks}, Max Marks: {max_marks}, Percentage: {percentage}, Status: {doc.status} \n\n\n")
