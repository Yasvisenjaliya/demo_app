import frappe
import json
from frappe import _

@frappe.whitelist(allow_guest=True)
def create_student_with_subjects():
    try:
        # Get request data
        if frappe.request and frappe.request.data:
            data = json.loads(frappe.request.data)
            frappe.logger().info(f"Received Data: {data}")

            student_data = data.get("student_data")
            subject_data = data.get("subject_data")

        if isinstance(student_data, str):
            student_data = json.loads(student_data)
        if isinstance(subject_data, str):
            subject_data = json.loads(subject_data)

        if not student_data or not subject_data:
            return {"status": "error", "message": _("Missing student data or subject data.")}

        # Create Student Record
        student = frappe.get_doc({
            "doctype": "Student",
            "first_name": student_data.get("first_name"),
            "middle_name": student_data.get("middle_name"),
            "last_name": student_data.get("last_name"),
            "email": student_data.get("email"),
            "grade": student_data.get("grade"),
            "status": student_data.get("status"),
        })
        student.insert(ignore_permissions=True)

        # Append subjects using the new child table
        for subject in subject_data:
            student.append("subjects", {  # Ensure "subjects" matches the child table field in Student
                "subject": subject.get("subject_name"),
                "subject_code": subject.get("subject_code")
            })

        student.save(ignore_permissions=True)
        frappe.db.commit()

        return {"status": "success", "message": _("Student record created with subjects successfully")}

    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Error creating student with subjects")
        return {"status": "error", "message": str(e)}
