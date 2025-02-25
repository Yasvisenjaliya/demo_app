# import frappe

# def send_email_on_validate(doc, method):
#     """
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
