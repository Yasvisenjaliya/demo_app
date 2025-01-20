# from frappe.model.document import Document
# import frappe

# # Assuming the base 'Student' functionality resides in this module
# # from demo_app.programing_module.doctype.student.student import Student

# from demo_app.programing_module.doctype.customize_student_doc.customize_student_doc import CustomizeStudentDoc

# class DCODEStudent(CustomizeStudentDoc):
#     def validate(self):
#         print("\n\n\n Hellooooooooooooooooooooooooooo \n\n\n")
#         return


# # demo_app/demo_app/programing_module/doctype/customize_student_doc/customize_student_doc


import frappe

def customer_count(doc, method):
    if doc.customer_group:
        customer_group_count = frappe.db.count('Customer', filters={'customer_group': doc.customer_group})
        doc.customer_group_count = customer_group_count

