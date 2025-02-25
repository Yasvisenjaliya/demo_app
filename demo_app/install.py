
# import frappe

# def after_install():
#     """This function will be executed after the app is installed."""
#     print("Running after install tasks.")

#     if not frappe.db.exists('Student', 'default_student'):
#         student_doc = frappe.get_doc({
#             'doctype': 'Student',
#             'name': 'default_student',  
#             'first_name': 'John',
#             'middle_name': 'Doe',
#             'last_name': 'Student',
#             'email': 'john.doe@example.com',
#             'grade': 'A',
#             'subject': 'Mathematics',
#         })
#         student_doc.insert()

#         print("Default Student record created.")
