# demo_app/notifications.py

import frappe

def get_notification_config():
    """Returns the notification configuration for demo_app."""
    return {
        "for_doctype": {
            "Student": {
                "subject": "Student Record Updated",
                "message": "The student record has been updated.",
                "actions": [
                    {
                        "do": "demo_app.notifications.send_notification",
                        "label": "Send Notification",
                        "method": "send_notification"
                    }
                ]
            }
        }
    }

def send_notification(doc, method):
    """Send notification for the student record update."""
    print(f"Sending notification for {doc.first_name} {doc.last_name}")
    
    # Send email notification
    frappe.sendmail(
        recipients=doc.email,
        subject="Student Record Updated",
        message=f"Dear {doc.first_name},\n\nYour student record has been updated."
    )
    
    # Display a message in the Frappe UI
    frappe.msgprint(f"Notification sent to {doc.first_name}.")
