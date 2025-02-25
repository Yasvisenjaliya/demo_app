# # Copyright (c) 2025, dcode and contributors
# # For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ServerSideScripting(Document):
    pass
#     def validate(self):
#         """
#     Send an email when the document is validated.
#     """
#     # Check if the email field is empty
#     if not doc.email:
#         frappe.msgprint("Email field is empty. Cannot send an email.")
#         return

#     # Construct the email subject and message
#     subject = f"Hello {doc.first_name}, Welcome!"
#     message = f"""
#         <p>Dear {doc.first_name} {doc.last_name or ''},</p>
#         <p>Thank you for joining us!</p>
#         <p>Your details are as follows:</p>
#         <ul>
#             <li>Email: {doc.email}</li>
#             <li>Mobile Number: {doc.mob_no or 'N/A'}</li>
#             <li>Date of Birth: {doc.dob or 'N/A'}</li>
#         </ul>
#         <p>Best Regards,<br>Your Company</p>
#     """

#     # Send the email
#     try:
#         frappe.sendmail(
#             recipients=[doc.email],
#             subject=subject,
#             message=message,
#             reference_doctype=doc.doctype,
#             reference_name=doc.name
#         )
#         frappe.msgprint(f"Email sent to {doc.email} successfully!")
#     except Exception as e:
#         # Log the error and notify the user
#         frappe.log_error(message=str(e), title="Email Sending Error")
#         frappe.msgprint(f"Failed to send email to {doc.email}. Please check the logs for more details.")

    
    
# 	# def validate(self):
#     #         get_document(self)
#             # self.add_tags_to_doc()
#             # frappe.msgprint(f"Tags added to {self.name}.")


# # def get_document(self):
      
#     # old_doc = self.get_doc_before_save()

#     # if old_doc.first_name != self.first_name:
#     #     frappe.msgprint(f"First Name has changed from '{old_doc.first_name}' to '{self.first_name}' ")


# #  first_name_changed = self.has_value_changed("first_name")

# #  if first_name_changed:
# #         frappe.msgprint(
# #             f"First Name changed '{self.get_doc_before_save().first_name}' to '{self.first_name}'"
# #         )

# #  doc = frappe.get_doc("Client Side Scripting", "CS-001")
# #  doc.first_name = "New Name" 
# #  doc.reload() 
# #  frappe.msgprint(f"First Name after reload: {doc.first_name}")  


# #   if self.has_value_changed("first_name"):
#             # try:
#             #     self.check_permission(permtype='write')
#             #     frappe.msgprint("First Name has been updated successfully.")
#             # except frappe.PermissionError:
#             #     frappe.throw("You do not have permission to update the First Name field.")



 
#             # self.notify_update()  
#             # frappe.msgprint("First Name updated and changes notified.")




#     #    doc = frappe.get_doc("Client Side Scripting", "CS-001")                                
#     #    title = f"{doc.first_name} {doc.last_name}"
#     #    frappe.msgprint(f"The custom title is: {title}")




#     # meta = frappe.get_meta('Client Side Scripting')
#     # custom_fields = meta.get_custom_fields()
#     # if custom_fields:
#     #     frappe.msgprint(f"Custom Fields: {custom_fields}")
#     # else:
#     #     frappe.msgprint("No custom fields found in Client Side Scripting doctype.")
    
    
#     # meta = frappe.get_meta('Client Side Scripting')
#     # if meta.has_field('msj'):
#     #     frappe.msgprint("Field 'msj' exists in Client Side Scripting doctype.")
#     # else:
#     #     frappe.msgprint("Field 'msj' does not exist in Client Side Scripting doctype.")
    
    
    
#     # frappe.delete_doc('Client Side Scripting', 'CS-002')

#     # frappe.rename_doc('Client Side Scripting', 'CS-006', 'CS-0012')
       


#     #    frappe.new_doc(doctype)

#     #    doc = frappe.new_doc('Client Side Scripting')
#     #    doc.first_name = 'John'
#     #    doc.last_name = 'Doe'
#     #    doc.age = 30

#     #    doc.insert()    
         



#     # create a new document
#     # frappe.get_doc(dict) 

    
#     # doc = frappe.get_doc({
#     #     'doctype': 'Client Side Scripting',
#     #      'first_name': 'John',  
#     #     'last_name': 'Doe',
#     #     'age': 30
#     # })
#     # doc.insert(
#     # )
#     # frappe.msgprint("New document has been created with name: {0}".format(doc.first_name))

#     # doc = frappe.get_doc('Client Side Scripting', 'John Doe')  # Fetch the document
#     # doc.delete()  # Delete the document
#     # frappe.db.commit()  # Commit the transaction to persist the deletion

      
# #   docs = frappe.get_all('Client Side Scripting', fields=['name'])
# #   doc_names = ", ".join([doc['name'] for doc in docs])  
# #   frappe.msgprint(f"{doc_names}")

     


  
    
#     # frappe.get_last_doc(doctype, filters, order_by)

#     # doc = frappe.get_last_doc(
#     #     'Client Side Scripting', 
#     #     order_by="modified desc"
#     # )
#     # frappe.msgprint(f"Last Document (Sorted): {doc.first_name}")
#     # frappe.msgprint(f"Last modified time: {doc.modified}")





#     # frappe.get_doc(doctype, name)

#     # doc = frappe.get_doc('Client Side Scripting', self.client_side_doc)
#     # frappe.msgprint("The first name is {0} and Age is {1}".format(doc.first_name, doc.age))

#     # doc = frappe.get_doc('Client Side Scripting', 'CS-001')
#     # doc.age = 23
#     # doc.save




                
#     # self.db_set('first_name', self.first_name)  

#     #     # Update and trigger real-time notifications
#     # self.db_set('first_name', self.first_name, notify=True)  # Update and notify clients

#     #     # Update and commit the changes directly to the database
#     # self.db_set('first_name', self.first_name, commit=True)  # Update and commit

#     #     # Update the 'first_name' without modifying the timestamp
#     # self.db_set('first_name', self.first_name, update_modified=False)




#     #  self.append("family_members", {
#     #         "name1": "John",
#     #         "age": 30,
#     #         "relation": "Brother"
#     #     })


#     # url = self.get_url()
#     # frappe.msgprint(f"The Desk URL for this document is: {url}")



#     # self.add_comment('Comment', text='Document validation triggered.')
#     # if self.has_value_changed('first_name'):
#     #         self.add_comment('Edit', text=f"First Name changed to {self.first_name}")
#     # user = frappe.session.user
#     # self.add_comment('Shared', text=f'{user} shared this document with the team.')
#     # frappe.msgprint('Comments added successfully!')



#     # self.add_seen()
#     # specific_user = 'john@doe.com'
#     # self.add_seen(specific_user)
#     # frappe.msgprint(f"{frappe.session.user} has been added to the seen list.")


#     # add_seen_to_doc(self)
#     # def add_seen_to_doc(doc):
#     #     doc.add_seen()
#     # frappe.msgprint(f"{frappe.session.user} has been added to the seen list.")



#     # def log_view(doc):
#     #     doc.add_viewed()
#     # frappe.msgprint(f"View logged for {frappe.session.user}.")




# # def add_tags_to_doc(doc):
# #         doc.add_tag('developer')
# #         doc.add_tag('frontend')

# # def get_document(doc):
# #     add_tags_to_doc(doc)
# #     frappe.msgprint(f"Tags added to {doc.name}.")

# #     doc = frappe.get_doc('Server Side Scripting', 'SER-021')
# #     doc.run_method('validate')
# #     tags = doc.get_tags()
# #     frappe.msgprint(f"Tags associated with {doc.name}: {tags}")



    
#         # def add_tags_to_doc(self):
#         #     self.add_tag('developer')
#         #     self.add_tag('frontend')
#         #     def send_emails(self, emails, message):
#         #      """Send emails to the provided list."""
#         #      for email in emails:
#         #     # Logic for sending email (could use frappe.sendmail)
#         #          frappe.sendmail(
#         #         recipients=email,
#         #         subject="Test Email",
#         #         message=message
#         #     )
#         #          frappe.msgprint(f"Email sent to {email}")



# #         # Fetch a parent document
# #     doc = frappe.get_doc('Sales Invoice', 'INV-0001')

# # # Get the child records associated with the 'items' table
# #     children = doc.get_children()

# # # Iterate over the children and print some fields
# #     for child in children:
# #         frappe.msgprint(f"Item: {child.item_name}, Quantity: {child.qty}")







#     #     records = frappe.db.get_list(
#     #     'Client Side Scripting',
#     #     filters={'enable': 1},  
#     #     fields=['name', 'first_name', 'email']  
#     # )
#     #     for record in records:
#     #         frappe.msgprint(f"Name: {record['name']}, First Name: {record['first_name']}, Email: {record['email']}")


#     # records = frappe.db.get_all(
#     #     'Client Side Scripting',
#     #     filters={'enable': 1}, 
#     #     fields=['name', 'first_name', 'email']  
#     # )
#     # for record in records:
#     #     frappe.msgprint(f"Name: {record['name']}, First Name: {record['first_name']}, Email: {record['email']}")



#     # email = frappe.db.get_value('Client Side Scripting', 'CS-001', 'email')
#     # frappe.msgprint(f"Email: {email}")



#     # first_name, email = frappe.db.get_value('Client Side Scripting', 'CS-001', ['first_name', 'email'])
#     # frappe.msgprint(f"Name: {first_name}, Email: {email}")


#     # client_name = frappe.db.get_value('Client Side Scripting', {'enable': 1}, 'name')
#     # frappe.msgprint(f"Enabled Client: {client_name}")


#     # email = frappe.db.get_single_value('Client Side Scripting', 'email')
#     # frappe.msgprint(f"Email: {email}")


#         # email = frappe.db.get_single_value('Client Side Scripting', 'email')
    
#         # if email:
#         #     frappe.msgprint(f"Email: {email}")
#         # else:
#         #     frappe.msgprint("Email not found.")


#         #   frappe.db.set_value('Client Side Scripting', 'CS-001', 'email', 'newemail@example.com')
#         #   frappe.msgprint("Email updated.")



#     # exists = frappe.db.exists('Client Side Scripting', 'yasvisenjaliya2@gmail.com', cache=True)
#     # exists = frappe.db.exists('Client Side Scripting', {"first_name":"john"})
    
#     # if exists:
#     #     frappe.msgprint("Record exists.")
#     # else:
#     #     frappe.msgprint("Record does not exist.")


#     # count = frappe.db.count('Client Side Scripting', filters={'enable': 1})
#     # frappe.msgprint(f"Count of enabled records: {count}")


#     # frappe.db.delete('Client Side Scripting', filters={'enable': 0})


#     # frappe.db.truncate('Client Side Scripting')



# #     doc = frappe.get_doc({
# #     'doctype': 'Client Side Scripting',
# #     'first_name': 'John',
# #     'last_name': 'Doe',
# #     'email': 'john.doe@example.com'
# #     })
# #     doc.insert()

# # frappe.db.commit()




#     # savepoint = frappe.db.savepoint("my_savepoint")

#     # try:
#     #     frappe.get_doc({
#     #         'doctype': 'Client Side Scripting',
#     #         'first_name': 'John',
#     #         'last_name': 'Doe'
#     #     }).insert()

#     #     frappe.db.commit()

#     # except Exception:
#     #     frappe.db.rollback(savepoint)


# #    result = frappe.db.sql("SELECT * FROM `tabClient Side Scripting` WHERE enable = 1", as_dict=True)
# #    print(result)  # Check if data is correct before saving


#     # result = frappe.db.sql("""
#     #     SELECT COUNT(*) AS count
#     #     FROM `tabClient Side Scripting`
#     #     WHERE name = %s
#     # """, ('CS-001',), as_dict=True)

#     # if result[0]['count'] > 0:
#     #     frappe.msgprint("Record exists.")
#     # else:
#     #     frappe.msgprint("Record does not exist.")



#     # queries = {
#     #     "INSERT INTO `tabClient Side Scripting` (first_name, last_name) VALUES (%s, %s)": [('John', 'Doe')],
#     #     "UPDATE `tabClient Side Scripting` SET first_name = %s WHERE name = %s": [('Updated John', 'CS-001')]
#     # }

#     # for query, values in queries.items():
#     #     for value_tuple in values:
#     #         if None in value_tuple:
#     #             frappe.throw(f"Found None value in query: {query} with values: {value_tuple}")

#     # frappe.db.multisql(queries)
#     # frappe.msgprint("Multiple records inserted and updated.")




#     # frappe.db.rename_table('SER-012', 'SER-003')





# #     frappe.db.sql("""
# #     ALTER TABLE `tabServer Side Scripting`
# #     ADD COLUMN `price` VARCHAR(255);
# # """)



#     # frappe.db.add_index('tabServer Side Scripting', 'age')


#     # frappe.db.add_unique('tabServer Side Scripting', 'name')




















