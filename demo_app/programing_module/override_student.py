import frappe
from your_app.customize_student_doc.doc import CustomizeStudentDoc  # Import the original class

class CustomStudentDocOverride(CustomizeStudentDoc):
    def validate(self):
        """
        Override the validate method to calculate percentage and update status.
        """
        if not self.marks:  # Ensure there are marks in the child table
            frappe.throw("No marks found in the child table.")

        # Calculate total marks and percentage
        total_marks = sum([row.marks for row in self.marks])
        max_marks = len(self.marks) * 100  # Assuming each subject has a maximum of 100 marks
        percentage = (total_marks / max_marks) * 100

        # Update the percentage field
        self.percentage = percentage

        # Update the status field based on the percentage
        if percentage < 33:
            self.status = "Failed"
        elif 33 <= percentage <= 50:
            self.status = "Pass"
        else:
            self.status = "Excellent"
