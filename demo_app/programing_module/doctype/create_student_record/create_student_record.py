# import frappe
# from frappe import _

# @frappe.whitelist(allow_guest=True)
# def create_student_with_courses(student_data, course_data):
#     """
#     Creates a new 'Create Student Record' record and inserts the related course data into the child table.

#     Args:
#         student_data (dict): A dictionary containing the student details (student_name, email, phone_number, etc.).
#         course_data (list): A list of dictionaries containing the details of the courses and grades.
    
#     Returns:
#         dict: The created 'Create Student Record' along with child course details.
#     """
#     try:
#         # Create 'Create Student Record' record
#         student_record = frappe.get_doc({
#             "doctype": "Create Student Record",  # The new custom doctype
#             "student_name": student_data.get("student_name"),
#             "email": student_data.get("email"),
#             "phone_number": student_data.get("phone_number"),
#         })
#         student_record.insert()

#         # Create child table records (Student Course Details)
#         for course in course_data:
#             course_detail = frappe.get_doc({
#                 "doctype": "Student Course Details",
#                 "parent": student_record.name,
#                 "parenttype": "Create Student Record",  # Parent doctype
#                 "parentfield": "student_course_details",  # Child table field in 'Create Student Record'
#                 "course_name": course.get("course_name"),
#                 "grade": course.get("grade"),
#                 "remark": course.get("remark"),
#             })
#             course_detail.insert()

#         # Return success response with student details
#         return {
#             "status": "success",
#             "message": _("Create Student Record and course data created successfully."),
#             "student_record": student_record.as_dict(),
#             "course_details": [course.as_dict() for course in student_record.student_course_details],
#         }
#     except Exception as e:
#         return {
#             "status": "error",
#             "message": str(e),
#         }
