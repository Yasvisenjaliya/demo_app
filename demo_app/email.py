# # demo_app/email.py

# import frappe
# from frappe.email.smtp import sendmail

# def send_custom_email(recipients, subject, message, **kwargs):
#     """Custom email send function to override Frappe's default email sending."""

#     if isinstance(recipients, str):
#         recipients = [recipients]

#     frappe.logger().info(f"Sending email to: {recipients}, Subject: {subject}")

    
#     sendmail(
#         recipients=recipients,
#         subject=subject,
#         message=message,
#         **kwargs
#     )

#     frappe.msgprint(f"Custom email sent to {', '.join(recipients)}")


# demo_app/email.py

# import frappe
# from frappe.email.utils import get_sender_details as frappe_get_sender_details

# def get_sender_details():
#     """Custom sender details override."""
#     sender_email, sender_name = frappe_get_sender_details()
    
#     if sender_email == "default@example.com":
#         sender_email = "patelyasu637@gmail.com"
#         sender_name = "Custom Sender"

#     return sender_email, sender_name

